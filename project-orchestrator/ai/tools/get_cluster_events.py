import json
import subprocess


def get_cluster_events():

    cmd = [
        "kubectl",
        "get",
        "events",
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

    events = []

    for item in data.get("items", []):

        events.append({
            "namespace": item["metadata"]["namespace"],
            "reason": item.get("reason"),
            "message": item.get("message"),
            "type": item.get("type"),
            "time": item.get("lastTimestamp")
                or item["metadata"].get("creationTimestamp")
        })

    return events


if __name__ == "__main__":
    print(json.dumps(get_cluster_events(), indent=2))