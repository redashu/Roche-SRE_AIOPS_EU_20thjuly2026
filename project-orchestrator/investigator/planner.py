import json
import boto3
from botocore.exceptions import ClientError

try:
    from investigator.planner_prompt import PLANNER_PROMPT
except ModuleNotFoundError:
    from planner_prompt import PLANNER_PROMPT
import os
import sys
import re


sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

REGION = "ap-south-1"
MODEL_ID = "meta.llama3-8b-instruct-v1:0"

client = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)

# --------------------------------------------------
# Planner
# --------------------------------------------------

class InvestigationPlanner:

    def __init__(self):

        self.client = client

        self.model_id = MODEL_ID

    # ----------------------------------------------

    def create_plan(self, question):

        try:

            response = self.client.converse(

                modelId=self.model_id,

                system=[
                    {
                        "text": PLANNER_PROMPT
                    }
                ],

                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": question
                            }
                        ]
                    }
                ],

                inferenceConfig={

                    "temperature": 0,

                    "topP": 0.1,

                    "maxTokens": 512

                }

            )

            planner_response = response["output"]["message"]["content"][0]["text"]

            print("\n==============================")
            print("Planner Raw Response")
            print("==============================")
            print(planner_response)
            
            match = re.search(
                r"\{.*\}",
                planner_response,
                re.DOTALL
            )

            if not match:
                raise RuntimeError("Planner did not return JSON.")

            json_text = match.group(0)

            plan = json.loads(json_text)

            self.validate_plan(plan)

            return plan

        except json.JSONDecodeError:

            raise RuntimeError(
                "Planner returned invalid JSON."
            )

        except ClientError as e:

            raise RuntimeError(
                e.response["Error"]["Message"]
            )

    # ----------------------------------------------

    def validate_plan(self, plan):

        if not isinstance(plan, dict):

            raise RuntimeError(
                "Planner output must be a JSON object."
            )

        if "investigation" not in plan:

            raise RuntimeError(
                "Missing investigation section."
            )

        if not isinstance(plan["investigation"], list):

            raise RuntimeError(
                "Investigation must be a list."
            )

        if len(plan["investigation"]) == 0:

            raise RuntimeError(
                "Investigation cannot be empty."
            )

        for step in plan["investigation"]:

            if "tool" not in step:

                raise RuntimeError(
                    "Missing tool."
                )

            if "reason" not in step:

                raise RuntimeError(
                    "Missing reason."
                )

        return True

    # ----------------------------------------------

    def print_plan(self, plan):

        print("\n==============================")
        print("Investigation Plan")
        print("==============================")

        for i, step in enumerate(plan["investigation"], start=1):

            print(f"\nStep {i}")

            print(f"Tool   : {step['tool']}")

            print(f"Reason : {step['reason']}")


# --------------------------------------------------
# CLI
# --------------------------------------------------

if __name__ == "__main__":

    planner = InvestigationPlanner()

    while True:

        question = input("\nAsk : ").strip()

        if question.lower() == "exit":

            break

        plan = planner.create_plan(question)

        planner.print_plan(plan)