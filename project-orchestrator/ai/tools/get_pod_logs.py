import subprocess


def get_pod_logs(namespace, pod_name):

    cmd = [
        "kubectl",
        "logs",
        pod_name,
        "-n",
        namespace,
        "--tail=100"
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout


if __name__ == "__main__":

    namespace = input("Namespace : ")
    pod = input("Pod Name : ")

    print(get_pod_logs(namespace, pod))