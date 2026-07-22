import json
import boto3
from botocore.exceptions import ClientError

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------
REGION = "ap-south-1"
MODEL_ID = "meta.llama3-8b-instruct-v1:0"

# ----------------------------------------------------
# Create Bedrock Runtime Client
# ----------------------------------------------------
client = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)

# ----------------------------------------------------
# Conversation Memory
# ----------------------------------------------------
conversation = []

print("=" * 70)
print(" Amazon Bedrock - Meta Llama 3 (Memory Enabled)")
print(" Type 'exit' to quit")
print("=" * 70)

while True:

    # ------------------------------------------------
    # Take User Input
    # ------------------------------------------------
    user_prompt = input("\nYou : ").strip()

    if user_prompt.lower() in ["exit", "quit"]:
        print("\nGoodbye!")
        break

    if not user_prompt:
        continue

    # ------------------------------------------------
    # Store User Message
    # ------------------------------------------------
    conversation.append({
        "role": "user",
        "content": user_prompt
    })

    # ------------------------------------------------
    # Build Prompt from Memory
    # ------------------------------------------------
    formatted_prompt = "<|begin_of_text|>\n"

    for message in conversation:

        formatted_prompt += (
            f"<|start_header_id|>{message['role']}<|end_header_id|>\n"
            f"{message['content']}\n"
            "<|eot_id|>\n"
        )

    formatted_prompt += "<|start_header_id|>assistant<|end_header_id|>\n"

    # ------------------------------------------------
    # Request Payload
    # ------------------------------------------------
    request_body = {
        "prompt": formatted_prompt,
        "max_gen_len": 512,
        "temperature": 0.2,
        "top_p": 0.9
    }

    try:

        response = client.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(request_body),
            accept="application/json",
            contentType="application/json"
        )

        response_body = json.loads(response["body"].read())

        ai_response = response_body["generation"]

        print("\nAI :")
        print(ai_response)
        print("\n========== Token Usage ==========")
        print(f"Input Tokens  : {response_body['prompt_token_count']}")
        print(f"Output Tokens : {response_body['generation_token_count']}")
        print("=================================")

        # --------------------------------------------
        # Store AI Response in Memory
        # --------------------------------------------
        conversation.append({
            "role": "assistant",
            "content": ai_response
        })

    except ClientError as e:
        print(f"\nAWS Error : {e.response['Error']['Message']}")

    except Exception as e:
        print(f"\nUnexpected Error : {e}")