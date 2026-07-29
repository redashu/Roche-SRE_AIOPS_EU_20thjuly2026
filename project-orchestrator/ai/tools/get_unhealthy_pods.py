import json
import subprocess


def get_unhealthy_pods():

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

    unhealthy = []

    for item in data.get("items", []):

        phase = item["status"]["phase"]

        restart_count = sum(
            c.get("restartCount", 0)
            for c in item["status"].get("containerStatuses", [])
        )

        waiting_reason = ""

        for c in item["status"].get("containerStatuses", []):

            state = c.get("state", {})

            if "waiting" in state:
                waiting_reason = state["waiting"].get("reason", "")

        if (
            phase != "Running"
            or restart_count > 0
            or waiting_reason != ""
        ):

            unhealthy.append({
                "namespace": item["metadata"]["namespace"],
                "pod": item["metadata"]["name"],
                "phase": phase,
                "reason": waiting_reason,
                "restart_count": restart_count
            })

    return unhealthy


if __name__ == "__main__":
    print(json.dumps(get_unhealthy_pods(), indent=2))