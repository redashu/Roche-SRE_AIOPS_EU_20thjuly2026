import boto3
from botocore.exceptions import ClientError

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

    system_prompt = """
You are an AI Kubernetes Tool Router.

Your ONLY job is to select the correct tool.

Available Tool

Tool Name:
get_all_pods

Description:
Returns complete Kubernetes Pod information from all namespaces.

Supported Questions:

- show pods
- list pods
- list all pods
- running pods
- pod status
- pod names
- namespaces of pods
- pod ip
- node name
- restart count
- any Kubernetes pod related question

Rules

1. If the question can be answered using this tool, return exactly:

get_all_pods

2. Otherwise return exactly:

NO_TOOL

3. Never explain.

4. Never answer the user's question.

5. Never generate code.

6. Return only ONE WORD.
"""

    try:

        response = client.converse(

            modelId=MODEL_ID,

            system=[
                {
                    "text": system_prompt
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

        answer = response["output"]["message"]["content"][0]["text"]

        answer = answer.strip()

        print(f"\nLLM Response : {answer}")

        if answer == "get_all_pods":
            return "get_all_pods"

        return "NO_TOOL"

    except ClientError as e:

        raise Exception(
            e.response["Error"]["Message"]
        )


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    while True:

        question = input("\nAsk : ")

        if question.lower() == "exit":
            break

        tool = select_tool(question)

        print("\nSelected Tool :", tool)