from loader import DocumentLoader


class TextChunker:

    def __init__(
        self,
        chunk_size=500,
        chunk_overlap=100
    ):

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    # --------------------------------------------------
    # Public API
    # --------------------------------------------------
    def chunk(self, documents, strategy="fixed"):

        if strategy == "fixed":
            return self.fixed_chunk_documents(documents)

        elif strategy == "recursive":
            return self.recursive_chunk_documents(documents)

        elif strategy == "semantic":
            return self.semantic_chunk_documents(documents)

        elif strategy == "markdown":
            return self.markdown_chunk_documents(documents)

        elif strategy == "yaml":
            return self.yaml_chunk_documents(documents)

        elif strategy == "html":
            return self.html_chunk_documents(documents)

        else:
            raise Exception(f"Unknown chunking strategy : {strategy}")

    # --------------------------------------------------
    # Fixed Chunking
    # --------------------------------------------------
    def fixed_chunk_documents(self, documents):

        chunks = []

        chunk_id = 1

        for document in documents:

            text = document["content"]

            start = 0

            chunk_number = 1

            while start < len(text):

                end = start + self.chunk_size

                chunk_text = text[start:end]

                chunks.append({

                    "chunk_id": chunk_id,

                    "document_id": document["document_id"],

                    "filename": document["filename"],

                    "chunk_number": chunk_number,

                    "content": chunk_text,

                    "metadata": {}

                })

                chunk_id += 1

                chunk_number += 1

                start += self.chunk_size - self.chunk_overlap

        return chunks

    # --------------------------------------------------
    # Recursive Chunking
    # --------------------------------------------------
    def recursive_chunk_documents(self, documents):

        raise NotImplementedError(
            "Recursive Chunking will be implemented later."
        )

    # --------------------------------------------------
    # Semantic Chunking
    # --------------------------------------------------
    def semantic_chunk_documents(self, documents):

        raise NotImplementedError(
            "Semantic Chunking will be implemented later."
        )

    # --------------------------------------------------
    # Markdown Chunking
    # --------------------------------------------------
    def markdown_chunk_documents(self, documents):

        raise NotImplementedError(
            "Markdown Chunking will be implemented later."
        )

    # --------------------------------------------------
    # YAML Chunking
    # --------------------------------------------------
    def yaml_chunk_documents(self, documents):

        raise NotImplementedError(
            "YAML Chunking will be implemented later."
        )

    # --------------------------------------------------
    # HTML Chunking
    # --------------------------------------------------
    def html_chunk_documents(self, documents):

        raise NotImplementedError(
            "HTML Chunking will be implemented later."
        )


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

    print("=" * 70)
    print(f"Total Chunks : {len(chunks)}")
    print("=" * 70)

    for chunk in chunks[:10]:

        print(f"\nChunk ID      : {chunk['chunk_id']}")
        print(f"Document ID   : {chunk['document_id']}")
        print(f"Filename      : {chunk['filename']}")
        print(f"Chunk Number  : {chunk['chunk_number']}")

        print("-" * 70)

        print(chunk["content"])

        print("-" * 70)