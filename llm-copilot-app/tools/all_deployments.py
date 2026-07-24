import json
import subprocess


def get_all_deployments():

    cmd = [
        "kubectl",
        "get",
        "deployments",
        "-A",
        "-o",
        "json"
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    data = json.loads(result.stdout)

    deployments = []

    for item in data.get("items", []):

        deployments.append({
            "namespace": item["metadata"]["namespace"],
            "name": item["metadata"]["name"],
            "replicas": item["spec"].get("replicas"),
            "ready_replicas": item["status"].get("readyReplicas", 0),
            "available_replicas": item["status"].get("availableReplicas", 0)
        })

    return deployments


if __name__ == "__main__":

    print(
        json.dumps(
            get_all_deployments(),
            indent=2
        )
    )