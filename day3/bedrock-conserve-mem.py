import boto3

REGION = "ap-south-1"
MODEL_ID = "meta.llama3-8b-instruct-v1:0"

client = boto3.client(
    "bedrock-runtime",
    region_name=REGION
)

messages = []

system = [
    {
        "text": "You are an experienced AWS Solutions Architect."
    }
]

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    # Add user message
    messages.append(
        {
            "role": "user",
            "content": [
                {
                    "text": question
                }
            ]
        }
    )

    response = client.converse(

        modelId=MODEL_ID,

        system=system,

        messages=messages,

        inferenceConfig={
            "temperature":0,
            "topP":0.9,
            "maxTokens":512
        }

    )

    answer = response["output"]["message"]["content"][0]["text"]

    print("\nAssistant :\n")

    print(answer)

    # Save assistant response
    messages.append(
        response["output"]["message"]
    )