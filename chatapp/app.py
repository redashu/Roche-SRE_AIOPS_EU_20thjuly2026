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
# Bedrock Runtime Client
# ----------------------------------------------------
client = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)


# ----------------------------------------------------
# Converse API - now takes the FULL conversation so
# the model can see previous turns and handle
# follow-up questions correctly.
# ----------------------------------------------------
def call_bedrock(messages):
    try:
        response = client.converse(
            modelId=MODEL_ID,
            messages=messages,
            inferenceConfig={
                "temperature": 0.2,
                "topP": 0.9,
                "maxTokens": 512
            }
        )
        return response["output"]["message"]["content"][0]["text"]

    except ClientError as e:
        return f"AWS Error: {e.response['Error']['Message']}"

    except Exception as e:
        return f"Unexpected Error: {e}"


# ----------------------------------------------------
# Home
# ----------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    history = session.get("history", [])
    return render_template("index.html", history=history)


# ----------------------------------------------------
# Chat
# ----------------------------------------------------
@app.route("/chat", methods=["POST"])
def chat():
    user_prompt = request.form.get("prompt", "").strip()

    if user_prompt:
        # Full conversation kept in Bedrock Converse message format,
        # so it doubles as both the API payload and the display history.
        history = session.get("history", [])

        history.append({
            "role": "user",
            "content": [{"text": user_prompt}]
        })

        ai_response = call_bedrock(history)

        history.append({
            "role": "assistant",
            "content": [{"text": ai_response}]
        })

        session["history"] = history

    return redirect(url_for("index"))


# ----------------------------------------------------
# Clear Chat
# ----------------------------------------------------
@app.route("/clear", methods=["POST"])
def clear():
    session.pop("history", None)
    return redirect(url_for("index"))


# ----------------------------------------------------
# Run
# ----------------------------------------------------
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )