import json
import subprocess


def get_all_pods():

    cmd = [
        "kubectl",
        "get",
        "pods",
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

    pods = []

    for item in data.get("items", []):

        pods.append({
            "namespace": item["metadata"]["namespace"],
            "name": item["metadata"]["name"],
            "status": item["status"]["phase"]
        })

    return pods


if __name__ == "__main__":

    print(
        json.dumps(
            get_all_pods(),
            indent=2
        )
    )