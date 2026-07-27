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

from ai.tools.tool_selector import select_tool
from ai.tools.tool_registry import execute_tool

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
# # Tool Registry
# # (Easy to add more tools later)
# # ----------------------------------------------------
# TOOL_REGISTRY = {
#     "get_all_pods": get_all_pods
# }

# # ----------------------------------------------------
# # Execute Tool
# # ----------------------------------------------------
# def execute_tool(tool_name):

#     tool = TOOL_REGISTRY.get(tool_name)

#     if tool is None:
#         return None

#     return tool()


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
- Explain the results professionally.
- Use markdown bullet points or tables whenever appropriate.
- Do not mention JSON unless the user explicitly asks.
"""


def summarize(user_question, tool_output):

    user_prompt = f"""
User Question:

{user_question}

Tool Output:

{json.dumps(tool_output, indent=2)}

Generate the best possible answer using ONLY the tool output.
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

        raise RuntimeError(
            e.response["Error"]["Message"]
        )


# ----------------------------------------------------
# Reusable Function
# (CLI + Flask both call this)
# ----------------------------------------------------
def process_question(user_question):

    try:

        # -----------------------------
        # Tool Selection
        # -----------------------------
        tool_name = select_tool(user_question)

        if tool_name == "NO_TOOL":

            return {
                "success": False,
                "tool": None,
                "tool_output": None,
                "answer": "Sorry, I couldn't find a suitable Kubernetes tool for your request."
            }

        # -----------------------------
        # Tool Execution
        # -----------------------------
        tool_output = execute_tool(tool_name)

        if tool_output is None:

            return {
                "success": False,
                "tool": tool_name,
                "tool_output": None,
                "answer": "Tool execution failed."
            }

        # -----------------------------
        # Response Generation
        # -----------------------------
        answer = summarize(
            user_question,
            tool_output
        )

        return {

            "success": True,

            "tool": tool_name,

            "tool_output": tool_output,

            "answer": answer

        }

    except Exception as e:

        return {

            "success": False,

            "tool": None,

            "tool_output": None,

            "answer": str(e)

        }


# ----------------------------------------------------
# CLI (Only for testing)
# Flask will NOT use this.
# ----------------------------------------------------
def main():

    print("\nKubernetes AI Assistant")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Ask : ").strip()

        if question.lower() in ["exit", "quit"]:

            print("\nGoodbye!")
            break

        result = process_question(question)

        print("\nSelected Tool :", result["tool"])

        print("\n" + "=" * 80)
        print(result["answer"])
        print("=" * 80)


if __name__ == "__main__":
    main()