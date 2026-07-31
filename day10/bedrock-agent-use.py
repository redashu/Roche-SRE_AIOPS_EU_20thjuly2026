import uuid
import boto3

# --------------------------------------------------
# Configuration
# --------------------------------------------------

REGION = "eu-central-1"

AGENT_ID = "LVK0CZUMV1"

AGENT_ALIAS_ID = "BIZ5ASESNS"

# Same session for the entire conversation
SESSION_ID = str(uuid.uuid4())

# --------------------------------------------------
# Bedrock Agent Runtime
# --------------------------------------------------

client = boto3.client(
    service_name="bedrock-agent-runtime",
    region_name=REGION
)

print("=" * 80)
print("AWS Bedrock Agent")
print(f"Session : {SESSION_ID}")
print("Type 'exit' to quit.")
print("=" * 80)

# --------------------------------------------------
# Chat Loop
# --------------------------------------------------

while True:

    question = input("\nAsk : ").strip()

    if question.lower() == "exit":
        break

    response = client.invoke_agent(

        agentId=AGENT_ID,

        agentAliasId=AGENT_ALIAS_ID,

        sessionId=SESSION_ID,

        inputText=question

    )

    print("\nAgent\n")

    event_stream = response["completion"]

    for event in event_stream:

        if "chunk" in event:

            print(

                event["chunk"]["bytes"].decode("utf-8"),

                end=""

            )

    print()