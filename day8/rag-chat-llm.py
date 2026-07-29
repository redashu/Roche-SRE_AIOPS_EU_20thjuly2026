import boto3

from retriever import Retriever
from prompt_builder import PromptBuilder


class RAGChat:

    # --------------------------------------------------
    # Configuration
    # --------------------------------------------------

    MODEL_ID = "meta.llama3-8b-instruct-v1:0"

    def __init__(self, region="ap-south-1"):

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=region
        )

        self.retriever = Retriever()

        self.prompt_builder = PromptBuilder()

    # --------------------------------------------------
    # Invoke Bedrock Converse API
    # --------------------------------------------------

    def generate_answer(self, payload):

        response = self.client.converse(

            modelId=self.MODEL_ID,

            system=payload["system"],

            messages=payload["messages"],

            inferenceConfig={

                "temperature": 0,

                "topP": 0.9,

                "maxTokens": 512

            }

        )

        return response["output"]["message"]["content"][0]["text"]

    # --------------------------------------------------
    # Ask Question
    # --------------------------------------------------

    def ask(self, question):

        print("\nSearching Knowledge Base...")

        chunks = self.retriever.retrieve(

            question,

            k=5

        )

        print(f"Retrieved {len(chunks)} chunks.")

        payload = self.prompt_builder.build(

            question,

            chunks

        )

        print("\nGenerating Answer...\n")

        answer = self.generate_answer(

            payload

        )

        return answer


# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":

    rag = RAGChat()

    print("\nKubernetes RAG Assistant")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Ask : ").strip()

        if question.lower() == "exit":
            break

        answer = rag.ask(question)

        print("=" * 80)

        print(answer)

        print("=" * 80)