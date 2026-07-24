import json
import subprocess


def get_all_services():

    cmd = [
        "kubectl",
        "get",
        "services",
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

    services = []

    for item in data.get("items", []):

        services.append({
            "namespace": item["metadata"]["namespace"],
            "name": item["metadata"]["name"],
            "type": item["spec"]["type"],
            "cluster_ip": item["spec"].get("clusterIP"),
            "ports": item["spec"].get("ports", [])
        })

    return services


if __name__ == "__main__":

    print(
        json.dumps(
            get_all_services(),
            indent=2
        )
    )