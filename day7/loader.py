import os
import yaml
from bs4 import BeautifulSoup


class DocumentLoader:

    SUPPORTED_EXTENSIONS = [
        ".html",
        ".css",
        ".yaml",
        ".yml",
        ".txt",
        ".md"
    ]

    def __init__(self, knowledge_path):

        self.knowledge_path = knowledge_path

    # --------------------------------------------------
    # Load all supported documents
    # --------------------------------------------------
    def load(self):

        documents = []

        document_id = 1

        for root, dirs, files in os.walk(self.knowledge_path):

            files.sort()

            for file in files:

                extension = os.path.splitext(file)[1].lower()

                if extension not in self.SUPPORTED_EXTENSIONS:
                    continue

                filepath = os.path.join(root, file)

                content = self.read_file(
                    filepath,
                    extension
                )

                documents.append({

                    "document_id": document_id,

                    "filename": file,

                    "filepath": filepath,

                    "source_type": extension.replace(".", ""),

                    "content": content,

                    "metadata": {}

                })

                document_id += 1

        return documents

    # --------------------------------------------------
    # Read individual file
    # --------------------------------------------------
    def read_file(self, filepath, extension):

        with open(filepath, "r", encoding="utf-8") as f:

            # ----------------------------
            # HTML
            # ----------------------------
            if extension == ".html":

                soup = BeautifulSoup(
                    f,
                    "html.parser"
                )

                return soup.get_text(
                    separator="\n",
                    strip=True
                )

            # ----------------------------
            # YAML
            # ----------------------------
            elif extension in [".yaml", ".yml"]:

                data = yaml.safe_load(f)

                return yaml.dump(
                    data,
                    sort_keys=False
                )

            # ----------------------------
            # CSS / TXT / Markdown
            # ----------------------------
            else:

                return f.read()


# --------------------------------------------------
# Test Loader
# --------------------------------------------------
if __name__ == "__main__":

    loader = DocumentLoader("knowledge")

    documents = loader.load()

    print("=" * 70)
    print(f"Documents Loaded : {len(documents)}")
    print("=" * 70)

    for document in documents:

        print(f"\nDocument ID : {document['document_id']}")
        print(f"Filename    : {document['filename']}")
        print(f"Type        : {document['source_type']}")

        print("-" * 70)

        print(document["content"][:300])

        print("-" * 70)