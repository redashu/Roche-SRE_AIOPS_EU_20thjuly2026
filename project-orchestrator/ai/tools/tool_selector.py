import boto3
from botocore.exceptions import ClientError

from ai.tools.system_prompt import SYSTEM_PROMPT
from ai.tools.tool_registry import TOOL_REGISTRY

# --------------------------------------------------
# Configuration
# --------------------------------------------------

REGION = "ap-south-1"
MODEL_ID = "meta.llama3-8b-instruct-v1:0"

client = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)

# --------------------------------------------------
# Tool Selection
# --------------------------------------------------

def select_tool(user_question):

    try:

        response = client.converse(

            modelId=MODEL_ID,

            system=[
                {
                    "text": SYSTEM_PROMPT
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
                "maxTokens": 10
            }

        )

        answer = response["output"]["message"]["content"][0]["text"].strip()

        print(f"\nLLM Response : {answer}")

        # Generic validation against registered tools
        if answer in TOOL_REGISTRY:
            return answer

        return "NO_TOOL"

    except ClientError as e:
        raise RuntimeError(
            e.response["Error"]["Message"]
        )

# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    while True:

        question = input("\nAsk : ").strip()

        if question.lower() == "exit":
            break

        tool = select_tool(question)

        print("\nSelected Tool :", tool)