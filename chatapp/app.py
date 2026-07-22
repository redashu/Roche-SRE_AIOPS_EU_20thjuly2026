import json
import boto3
from botocore.exceptions import ClientError
from flask import Flask, render_template, request, redirect, url_for, session

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------
REGION = "ap-south-1"
MODEL_ID = "meta.llama3-8b-instruct-v1:0"

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-key"  # needed for session storage

# ----------------------------------------------------
# Create Bedrock Runtime Client
# ----------------------------------------------------
client = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)


def call_bedrock_llama(user_prompt):
    """Send a prompt to the Bedrock Llama model and return the generated text."""

    formatted_prompt = f"""
<|begin_of_text|><|start_header_id|>user<|end_header_id|>
{user_prompt}
<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""

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
        return response_body["generation"].strip()

    except ClientError as e:
        return f"AWS Error: {e.response['Error']['Message']}"

    except Exception as e:
        return f"Unexpected Error: {e}"


@app.route("/", methods=["GET"])
def index():
    history = session.get("history", [])
    return render_template("index.html", history=history)


@app.route("/chat", methods=["POST"])
def chat():
    user_prompt = request.form.get("prompt", "").strip()

    if user_prompt:
        ai_response = call_bedrock_llama(user_prompt)

        history = session.get("history", [])
        history.append({"role": "user", "text": user_prompt})
        history.append({"role": "ai", "text": ai_response})
        session["history"] = history

    return redirect(url_for("index"))


@app.route("/clear", methods=["POST"])
def clear():
    session.pop("history", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)