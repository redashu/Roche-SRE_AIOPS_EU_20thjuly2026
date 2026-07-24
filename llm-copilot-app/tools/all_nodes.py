import json
import subprocess


def get_all_nodes():

    cmd = [
        "kubectl",
        "get",
        "nodes",
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

    nodes = []

    for item in data.get("items", []):

        nodes.append({
            "name": item["metadata"]["name"],
            "status": item["status"]["conditions"][-1]["type"],
            "kubernetes_version": item["status"]["nodeInfo"]["kubeletVersion"],
            "os": item["status"]["nodeInfo"]["osImage"],
            "architecture": item["status"]["nodeInfo"]["architecture"]
        })

    return nodes


if __name__ == "__main__":

    print(
        json.dumps(
            get_all_nodes(),
            indent=2
        )
    )