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

print("=" * 70)
print(" Amazon Bedrock - Meta Llama 3")
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
    # Meta Llama Prompt Format
    # ------------------------------------------------
    formatted_prompt = f"""
<|begin_of_text|><|start_header_id|>user<|end_header_id|>
{user_prompt}
<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""

    # ------------------------------------------------
    # Request Payload / prompt Builder 
    # ------------------------------------------------
    request_body = {
        "prompt": formatted_prompt,
        "max_gen_len": 512,
        "temperature": 0.2,
        "top_p": 0.9
    }

    try:
        # invoke api of bedrock-runtime 
        response = client.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(request_body),
            accept="application/json",
            contentType="application/json"
        )

        response_body = json.loads(response["body"].read())

        print("\nAI  :")
        print(response_body["generation"])

    except ClientError as e:
        print(f"\nAWS Error : {e.response['Error']['Message']}")

    except Exception as e:
        print(f"\nUnexpected Error : {e}")