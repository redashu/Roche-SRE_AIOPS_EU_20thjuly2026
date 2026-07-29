import json
import faiss
import boto3
import numpy as np


class Retriever:

    MODEL_ID = "amazon.titan-embed-text-v2:0"

    def __init__(
        self,
        region="ap-south-1",
        index_file="data/faiss.index",
        metadata_file="data/chunks.json"
    ):

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=region
        )

        self.index_file = index_file
        self.metadata_file = metadata_file

        self.index = None
        self.metadata = None

        self.load_index()
        self.load_metadata()

    # --------------------------------------------------
    # Load FAISS Index
    # --------------------------------------------------
    def load_index(self):

        self.index = faiss.read_index(
            self.index_file
        )

    # --------------------------------------------------
    # Load Metadata
    # --------------------------------------------------
    def load_metadata(self):

        with open(
            self.metadata_file,
            "r",
            encoding="utf-8"
        ) as f:

            self.metadata = json.load(f)

    # --------------------------------------------------
    # Embed Query
    # --------------------------------------------------
    def embed_query(self, question):

        body = {

            "inputText": question,

            "dimensions": 1024,

            "normalize": True

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
    # Search FAISS
    # --------------------------------------------------
    def search(self, query_embedding, k=5):

        query = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = self.index.search(
            query,
            k
        )

        return distances[0], indices[0]

    # --------------------------------------------------
    # Retrieve
    # --------------------------------------------------
    def retrieve(self, question, k=5):

        query_embedding = self.embed_query(
            question
        )

        distances, indices = self.search(
            query_embedding,
            k
        )

        results = []

        for distance, index in zip(distances, indices):

            if index == -1:
                continue

            chunk = self.metadata[index].copy()

            chunk["score"] = float(distance)

            results.append(chunk)

        return results


# --------------------------------------------------
# Test
# --------------------------------------------------
if __name__ == "__main__":

    retriever = Retriever()

    while True:

        question = input("\nAsk : ")

        if question.lower() == "exit":
            break

        chunks = retriever.retrieve(
            question,
            k=5
        )

        print("\nRetrieved Chunks\n")

        print("=" * 80)

        for i, chunk in enumerate(chunks, start=1):

            print(f"\nResult #{i}")

            print(f"Filename : {chunk['filename']}")

            print(f"Chunk    : {chunk['chunk_number']}")

            print(f"Score    : {chunk['score']}")

            print("-" * 60)

            print(chunk["content"])

            print("-" * 60)