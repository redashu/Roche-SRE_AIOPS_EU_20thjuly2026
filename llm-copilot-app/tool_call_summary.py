import json
import boto3
import os
import sys
from botocore.exceptions import ClientError

# ----------------------------------------------------
# Add Project Root
# ----------------------------------------------------
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from tools.tool_selector import select_tool
from tools.all_pods import get_all_pods

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------
REGION = "ap-south-1"
MODEL_ID = "meta.llama3-8b-instruct-v1:0"

client = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)

# ----------------------------------------------------
# Execute Tool
# ----------------------------------------------------
def execute_tool(tool_name):

    if tool_name == "get_all_pods":
        return get_all_pods()

    return None


# ----------------------------------------------------
# Response Generator
# ----------------------------------------------------
SYSTEM_PROMPT = """
You are an experienced Kubernetes Administrator.

You have received verified structured data from a Kubernetes tool.

Rules:

- Answer ONLY using the tool output.
- Never invent or assume information.
- If the requested information is unavailable, clearly state that.
- Explain the results in a professional manner.
- Use markdown bullet points or tables whenever appropriate.
- Do not mention JSON unless the user explicitly asks for it.
"""


def summarize(user_question, tool_output):

    user_prompt = f"""
User Question:

{user_question}

Tool Output:

{json.dumps(tool_output, indent=2)}

Generate the best possible answer for the user using ONLY the tool output.
"""

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
                            "text": user_prompt
                        }
                    ]
                }
            ],

            inferenceConfig={
                "temperature": 0,
                "topP": 0.9,
                "maxTokens": 512
            }

        )

        return response["output"]["message"]["content"][0]["text"]

    except ClientError as e:
        raise RuntimeError(e.response["Error"]["Message"])


# ----------------------------------------------------
# Main
# ----------------------------------------------------
def main():

    user_question = input("\nAsk : ")

    tool_name = select_tool(user_question)

    print(f"\nSelected Tool : {tool_name}")

    if tool_name == "NO_TOOL":
        print("\nNo suitable tool found.")
        return

    tool_output = execute_tool(tool_name)

    print("\nGenerating Response...\n")

    answer = summarize(
        user_question,
        tool_output
    )

    print("=" * 80)
    print(answer)
    print("=" * 80)


if __name__ == "__main__":
    main()