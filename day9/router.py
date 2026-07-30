import boto3
from botocore.exceptions import ClientError

import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from investigator.router_prompt import ROUTER_SYSTEM_PROMPT


class QueryRouter:

    REGION = "ap-south-1"
    MODEL_ID = "meta.llama3-8b-instruct-v1:0"

    def __init__(self):

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=self.REGION
        )

    # --------------------------------------------------
    # Route User Question
    # --------------------------------------------------

    def route(self, user_question):

        try:

            response = self.client.converse(

                modelId=self.MODEL_ID,

                system=[
                    {
                        "text": ROUTER_SYSTEM_PROMPT
                    }
                ],

                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": user_question
                            }
                        ]
                    }
                ],

                inferenceConfig={
                    "temperature": 0,
                    "topP": 0.1,
                    "maxTokens": 5
                }

            )

            answer = (
                response["output"]["message"]["content"][0]["text"]
                .strip()
                .upper()
            )

            print(f"\nRouter Decision : {answer}")

            if answer == "RAG":
                return "RAG"

            return "LIVE"

        except ClientError as e:

            raise RuntimeError(
                e.response["Error"]["Message"]
            )


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    router = QueryRouter()

    while True:

        q = input("\nAsk : ").strip()

        if q.lower() == "exit":
            break

        print(router.route(q))