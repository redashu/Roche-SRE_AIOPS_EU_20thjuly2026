import boto3

REGION = "eu-central-1"
MODEL_ID = "arn:aws:bedrock:eu-central-1:992382386705:inference-profile/global.amazon.nova-2-lite-v1:0"

client = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)
user_input = input("type your prompt : ")
response = client.converse(

    modelId=MODEL_ID,

    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": user_input
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

print("\nResponse\n")

print(
    response["output"]["message"]["content"][0]["text"]
)