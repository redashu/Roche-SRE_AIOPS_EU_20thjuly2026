import boto3
from botocore.exceptions import ClientError


class BedrockRAG:

    def __init__(
        self,
        region,
        knowledge_base_id,
        model_arn
    ):

        self.client = boto3.client(
            service_name="bedrock-agent-runtime",
            region_name=region
        )

        self.knowledge_base_id = knowledge_base_id
        self.model_arn = model_arn

    # --------------------------------------------------
    # Ask Knowledge Base
    # --------------------------------------------------

    def ask(self, question):

        try:

            response = self.client.retrieve_and_generate(

                input={
                    "text": question
                },

                retrieveAndGenerateConfiguration={

                    "type": "KNOWLEDGE_BASE",

                    "knowledgeBaseConfiguration": {

                        "knowledgeBaseId": self.knowledge_base_id,

                        "modelArn": self.model_arn

                    }

                }

            )

            citations = []

            for citation in response.get("citations", []):

                generated = citation.get(
                    "generatedResponsePart",
                    {}
                )

                references = citation.get(
                    "retrievedReferences",
                    []
                )

                for ref in references:

                    source = {}

                    # -----------------------------
                    # Source Name
                    # -----------------------------
                    location = ref.get("location", {})

                    if "s3Location" in location:

                        source["document"] = (
                            location["s3Location"]["uri"]
                            .split("/")[-1]
                        )

                    elif "webLocation" in location:

                        source["document"] = (
                            location["webLocation"]["url"]
                        )

                    else:

                        source["document"] = "Unknown"

                    # -----------------------------
                    # Retrieved Content
                    # -----------------------------
                    source["content"] = ref.get(
                        "content",
                        {}
                    ).get(
                        "text",
                        ""
                    )

                    citations.append(source)

            return {

                "answer": response["output"]["text"],

                "citations": citations

            }

        except ClientError as e:

            raise RuntimeError(
                e.response["Error"]["Message"]
            )


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    REGION = "eu-central-1"

    KNOWLEDGE_BASE_ID = "BWUYMYJCYX"

    MODEL_ARN = (
        "arn:aws:bedrock:eu-central-1:992382386705:application-inference-profile/aexzy32u2wwn"
    )

    rag = BedrockRAG(

        region=REGION,

        knowledge_base_id=KNOWLEDGE_BASE_ID,

        model_arn=MODEL_ARN

    )

    while True:

        question = input("\nAsk : ").strip()

        if question.lower() == "exit":
            break

        result = rag.ask(question)

        print("\n" + "=" * 80)
        print("ANSWER")
        print("=" * 80)
        print(result["answer"])

        # if result["citations"]:

        #     print("\n" + "=" * 80)
        #     print("REFERENCES")
        #     print("=" * 80)

        #     for i, ref in enumerate(result["citations"], start=1):

        #         print(f"\n[{i}] Document")
        #         print(f"    {ref['document']}")

        #         print("\nRetrieved Content")
        #         print("-" * 60)
        #         print(ref["content"])
        #         print("-" * 60)