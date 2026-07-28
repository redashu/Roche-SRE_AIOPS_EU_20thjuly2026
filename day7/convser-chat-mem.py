import boto3

REGION = "eu-central-1"
MODEL_ID = "arn:aws:bedrock:eu-central-1:992382386705:application-inference-profile/61mfossvl54g"

TOKEN_LIMIT = 1000
KEEP_LAST_QA = 3

client = boto3.client(
    "bedrock-runtime",
    region_name=REGION
)

system = [{
    "text": "You are an experienced AWS Solutions Architect."
}]

messages = []

# Running summary
conversation_summary = ""

# Index of last message already summarized
summary_pointer = 0


# -------------------------------------------------------
# Actual Bedrock token usage
# -------------------------------------------------------
def current_tokens(response):
    """
    Uses Bedrock usage information if present.
    """
    usage = response.get("usage", {})

    return (
        usage.get("inputTokens", 0)
        + usage.get("outputTokens", 0)
    )


# -------------------------------------------------------
# Generate incremental summary
# -------------------------------------------------------
def update_summary():

    global conversation_summary
    global summary_pointer

    new_messages = messages[summary_pointer:]

    if not new_messages:
        return

    text = ""

    for msg in new_messages:

        role = msg["role"]

        content = msg["content"][0]["text"]

        text += f"{role.upper()}: {content}\n"

    prompt = f"""
Existing Summary:

{conversation_summary}

Update the summary with ONLY the following new conversation.

Keep:

- facts
- user preferences
- decisions
- pending tasks

Return ONLY the updated summary.

New Conversation:

{text}
"""

    response = client.converse(

        modelId=MODEL_ID,

        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],

        inferenceConfig={
            "temperature": 0,
            "maxTokens": 300
        }

    )

    conversation_summary = (
        response["output"]["message"]["content"][0]["text"]
    )

    summary_pointer = len(messages)


# -------------------------------------------------------
# Last N QA
# -------------------------------------------------------
def last_qa(messages, n=3):

    qa = []

    pairs = []

    i = 0

    while i < len(messages)-1:

        if (
            messages[i]["role"] == "user"
            and messages[i+1]["role"] == "assistant"
        ):

            pairs.append(messages[i])
            pairs.append(messages[i+1])

            i += 2

        else:
            i += 1

    return pairs[-2*n:]


# -------------------------------------------------------
# Compress Memory
# -------------------------------------------------------
def compress():

    global messages

    print("\n========== MEMORY COMPRESSION ==========")

    update_summary()

    latest = last_qa(messages, KEEP_LAST_QA)

    messages = [

        {
            "role":"user",
            "content":[
                {
                    "text":
f"""Conversation Summary

{conversation_summary}

Use the summary as previous context.
Do not repeat it.
Continue naturally."""
                }
            ]
        }

    ]

    messages.extend(latest)

    print("Summary Updated.")
    print("Keeping last", KEEP_LAST_QA, "Q&A")


# -------------------------------------------------------
# Chat
# -------------------------------------------------------
last_input_tokens = 0

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    # Compress BEFORE appending user question
    if last_input_tokens > TOKEN_LIMIT:
        compress()

    messages.append(
        {
            "role":"user",
            "content":[
                {
                    "text":question
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

    print("\nAssistant:\n")

    print(answer)

    messages.append(
        response["output"]["message"]
    )

    usage = response.get("usage", {})

    last_input_tokens = usage.get("inputTokens", 0)

    print(
        f"\nInput Tokens  : {usage.get('inputTokens',0)}"
    )
    print(
        f"Output Tokens : {usage.get('outputTokens',0)}"
    )
    print(
        f"Total Tokens  : {usage.get('totalTokens',0)}"
    )