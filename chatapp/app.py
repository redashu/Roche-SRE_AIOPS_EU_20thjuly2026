import boto3
from botocore.exceptions import ClientError
from flask import Flask, render_template, request, redirect, url_for, session

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

REGION = "ap-south-1"
MODEL_ID = "meta.llama3-8b-instruct-v1:0"

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-key"

# ----------------------------------------------------
# Bedrock Client
# ----------------------------------------------------

client = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)

# ----------------------------------------------------
# Converse API
# ----------------------------------------------------

def call_bedrock(messages):

    try:

        response = client.converse(

            modelId=MODEL_ID,

            system=[
                {
                    "text": "You are a helpful AI assistant."
                }
            ],

            messages=messages,

            inferenceConfig={

                "temperature":0.2,

                "topP":0.9,

                "maxTokens":512

            }

        )

        return response["output"]["message"]

    except ClientError as e:

        return {

            "role":"assistant",

            "content":[

                {

                    "text":f"AWS Error : {e.response['Error']['Message']}"

                }

            ]

        }

# ----------------------------------------------------
# Home
# ----------------------------------------------------

@app.route("/")
def index():

    messages = session.get("messages", [])

    history = []

    for msg in messages:

        history.append({

            "role":"user" if msg["role"]=="user" else "ai",

            "text":msg["content"][0]["text"]

        })

    return render_template(

        "index.html",

        history=history

    )

# ----------------------------------------------------
# Chat
# ----------------------------------------------------

@app.route("/chat", methods=["POST"])
def chat():

    prompt = request.form.get("prompt","").strip()

    if not prompt:

        return redirect(url_for("index"))

    messages = session.get("messages", [])

    user_message = {

        "role":"user",

        "content":[

            {

                "text":prompt

            }

        ]

    }

    messages.append(user_message)

    assistant_message = call_bedrock(messages)

    messages.append(assistant_message)

    session["messages"] = messages

    return redirect(url_for("index"))

# ----------------------------------------------------
# Clear
# ----------------------------------------------------

@app.route("/clear", methods=["POST"])
def clear():

    session.clear()

    return redirect(url_for("index"))

# ----------------------------------------------------
# Main
# ----------------------------------------------------

if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000

    )