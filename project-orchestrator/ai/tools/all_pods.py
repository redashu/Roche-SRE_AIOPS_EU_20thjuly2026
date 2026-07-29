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

        metadata = item.get("metadata", {})
        spec = item.get("spec", {})
        status = item.get("status", {})

        container_statuses = status.get("containerStatuses", [])

        ready = 0
        total = len(container_statuses)
        restart_count = 0

        images = []

        for container in container_statuses:

            if container.get("ready"):
                ready += 1

            restart_count += container.get("restartCount", 0)

            images.append(container.get("image"))

        pod = {

            "namespace": metadata.get("namespace"),

            "pod_name": metadata.get("name"),

            "status": status.get("phase"),

            "ready": f"{ready}/{total}",

            "restart_count": restart_count,

            "node": spec.get("nodeName"),

            "pod_ip": status.get("podIP"),

            "host_ip": status.get("hostIP"),

            "start_time": status.get("startTime"),

            "service_account": spec.get("serviceAccountName"),

            "qos_class": status.get("qosClass"),

            "images": images

        }

        pods.append(pod)

    return pods


if __name__ == "__main__":

    print(
        json.dumps(
            get_all_pods(),
            indent=2
        )
    )