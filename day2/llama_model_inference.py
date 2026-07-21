import boto3
import json
REGION = "ap-south-1"
MODEL_ID = "meta.llama3-8b-instruct-v1:0"
client = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)
user_prompt = "Hello, who are you?"
formatted_prompt = f"""
<|begin_of_text|><|start_header_id|>user<|end_header_id|>
{user_prompt}
<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""
request_body = {
    "prompt": formatted_prompt,
    "temperature": 0,
    "top_p": 0.9,
    "max_gen_len": 512
}
response = client.invoke_model(
    modelId=MODEL_ID,
    body=json.dumps(request_body),
    accept="application/json",
    contentType="application/json"
)
response_body = json.loads(
    response["body"].read()
)
print("\nResponse\n")
print(response_body["generation"])