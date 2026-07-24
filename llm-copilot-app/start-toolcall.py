import boto3
from botocore.exceptions import ClientError

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
# Tool Selection
# --------------------------------------------------

def select_tool(user_question):

    system_prompt = """
You are a Kubernetes Tool Selector.

Your ONLY task is to select the correct tool.

=========================================
AVAILABLE TOOL
=========================================

Tool Name:
get_all_pods

Description:
Returns Kubernetes POD information from ALL namespaces.

This tool ONLY works for PODS.

It CANNOT answer questions about:

- Nodes
- ConfigMaps
- Secrets
- Deployments
- StatefulSets
- DaemonSets
- Services
- Ingress
- PVC
- PV
- StorageClasses
- Jobs
- CronJobs
- Namespaces
- Events
- Cluster
- Kubernetes version
- Helm
- RBAC

=========================================
USE get_all_pods ONLY FOR
=========================================

- show pods
- list pods
- running pods
- pod status
- pod names
- pod namespace
- pod IP
- pod node
- pod restart count
- failed pods
- completed pods
- pending pods
- pods in namespace xyz

=========================================
MUST RETURN NO_TOOL FOR
=========================================

- show nodes
- running nodes
- list nodes
- node status

- list configmaps
- config map details
- show configmaps

- list deployments
- deployment status

- services
- ingress

- secrets

- namespaces

- storage classes

- pvc

- pv

- cluster information

- kubernetes version

=========================================
EXAMPLES
=========================================

Question:
show pods

Answer:
get_all_pods

Question:
running pods

Answer:
get_all_pods

Question:
pod restart count

Answer:
get_all_pods

Question:
pods in kube-system

Answer:
get_all_pods

Question:
show nodes

Answer:
NO_TOOL

Question:
running nodes

Answer:
NO_TOOL

Question:
print all config map details

Answer:
NO_TOOL

Question:
show deployments

Answer:
NO_TOOL

Question:
show services

Answer:
NO_TOOL

Question:
show namespaces

Answer:
NO_TOOL

=========================================
RULES
=========================================

1. Return exactly one value.

2. If the question is about PODS:

get_all_pods

3. Otherwise:

NO_TOOL

4. Never explain.

5. Never answer the question.

6. Output ONLY one of:

get_all_pods
NO_TOOL
"""

    try:

        response = client.converse(

            modelId=MODEL_ID,

            system=[
                {
                    "text": system_prompt
                }
            ],

            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": user_question
                        }
                    ]
                }
            ],

            inferenceConfig={
                "temperature": 0,
                "topP": 0.1,
                "maxTokens": 10
            }

        )

        answer = (
            response["output"]["message"]["content"][0]["text"]
            .strip()
            .replace(".", "")
            .replace("`", "")
            .split()[0]
        )

        print("\nLLM Response :", answer)

        if answer == "get_all_pods":
            return "get_all_pods"

        return "NO_TOOL"

    except ClientError as e:
        raise Exception(e.response["Error"]["Message"])


# --------------------------------------------------
# Test
# --------------------------------------------------

if __name__ == "__main__":

    while True:

        question = input("\nAsk : ")

        if question.lower() == "exit":
            break

        tool = select_tool(question)

        print("\nSelected Tool :", tool)