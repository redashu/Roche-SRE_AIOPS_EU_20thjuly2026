import os
import json
import boto3

from loader import DocumentLoader
from chunker import TextChunker


class BedrockEmbedder:

    MODEL_ID = "amazon.titan-embed-text-v2:0"

    def __init__(
        self,
        region="ap-south-1",
        dimensions=1024,
        normalize=True,
        output_file="data/embeddings.json"
    ):

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=region
        )

        self.dimensions = dimensions
        self.normalize = normalize
        self.output_file = output_file

    # --------------------------------------------------
    # Generate embeddings for all chunks
    # --------------------------------------------------
    def embed_chunks(self, chunks):

        embedded_chunks = []

        total = len(chunks)

        print("\nGenerating Embeddings...\n")

        for index, chunk in enumerate(chunks, start=1):

            print(f"[{index}/{total}] {chunk['filename']}")

            embedding = self.generate_embedding(
                chunk["content"]
            )

            chunk["embedding"] = embedding

            embedded_chunks.append(chunk)

        return embedded_chunks

    # --------------------------------------------------
    # Titan Embedding
    # --------------------------------------------------
    def generate_embedding(self, text):

        body = {

            "inputText": text,

            "dimensions": self.dimensions,

            "normalize": self.normalize

        }

        response = self.client.invoke_model(

            modelId=self.MODEL_ID,

            body=json.dumps(body),

            accept="application/json",

            contentType="application/json"

        )

        response_body = json.loads(
            response["body"].read()
        )

        return response_body["embedding"]

    # --------------------------------------------------
    # Save Embeddings
    # --------------------------------------------------
    def save_embeddings(self, embedded_chunks):

        os.makedirs(
            os.path.dirname(self.output_file),
            exist_ok=True
        )

        with open(
            self.output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                embedded_chunks,
                f,
                indent=2
            )

        print(f"\nEmbeddings saved to : {self.output_file}")

    # --------------------------------------------------
    # Load Existing Embeddings
    # --------------------------------------------------
    def load_embeddings(self):

        if not os.path.exists(self.output_file):
            return None

        with open(
            self.output_file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


# --------------------------------------------------
# Test
# --------------------------------------------------
if __name__ == "__main__":

    loader = DocumentLoader("knowledge")

    documents = loader.load()

    chunker = TextChunker(

        chunk_size=500,

        chunk_overlap=100

    )

    chunks = chunker.chunk(

        documents,

        strategy="fixed"

    )

    embedder = BedrockEmbedder()

    # -----------------------------------------
    # Check Existing Embeddings
    # -----------------------------------------
    existing = embedder.load_embeddings()

    if existing:

        print("\nExisting embeddings found.")

        print(f"Chunks : {len(existing)}")

    else:

        embedded_chunks = embedder.embed_chunks(chunks)

        embedder.save_embeddings(
            embedded_chunks
        )

        print("\nEmbedding completed.")

        print(f"Total Chunks : {len(embedded_chunks)}")