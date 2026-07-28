import os
import json
import faiss
import numpy as np


class FAISSStore:

    def __init__(
        self,
        index_file="data/faiss.index",
        metadata_file="data/chunks.json"
    ):

        self.index_file = index_file
        self.metadata_file = metadata_file

        self.index = None

    # --------------------------------------------------
    # Build Index
    # --------------------------------------------------
    def build_index(self, embedded_chunks):

        print("\nBuilding FAISS Index...\n")

        vectors = []

        metadata = []

        for chunk in embedded_chunks:

            vectors.append(chunk["embedding"])

            metadata.append({

                "chunk_id": chunk["chunk_id"],

                "document_id": chunk["document_id"],

                "filename": chunk["filename"],

                "chunk_number": chunk["chunk_number"],

                "content": chunk["content"]

            })

        vectors = np.array(
            vectors,
            dtype="float32"
        )

        dimension = vectors.shape[1]

        print(f"Embedding Dimension : {dimension}")

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(vectors)

        print(f"Vectors Indexed : {self.index.ntotal}")

        self.save(metadata)

    # --------------------------------------------------
    # Save Index
    # --------------------------------------------------
    def save(self, metadata):

        os.makedirs(
            os.path.dirname(self.index_file),
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            self.index_file
        )

        with open(
            self.metadata_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                metadata,
                f,
                indent=2
            )

        print("\nFAISS index saved.")

        print(f"Index    : {self.index_file}")

        print(f"Metadata : {self.metadata_file}")

    # --------------------------------------------------
    # Load Index
    # --------------------------------------------------
    def load(self):

        self.index = faiss.read_index(
            self.index_file
        )

        with open(
            self.metadata_file,
            "r",
            encoding="utf-8"
        ) as f:

            metadata = json.load(f)

        print("\nFAISS index loaded.")

        print(f"Vectors : {self.index.ntotal}")

        return metadata

    # --------------------------------------------------
    # Search
    # --------------------------------------------------
    def search(
        self,
        query_embedding,
        k=5
    ):

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
# Test
# --------------------------------------------------
if __name__ == "__main__":

    with open(
        "data/embeddings.json",
        "r",
        encoding="utf-8"
    ) as f:

        embedded_chunks = json.load(f)

    store = FAISSStore()

    store.build_index(
        embedded_chunks
    )

    metadata = store.load()

    print("\nFirst Metadata Record\n")

    print(metadata[0])