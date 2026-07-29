import subprocess


def describe_pods(namespace, pod_name):

    cmd = [
        "kubectl",
        "describe",
        "pod",
        pod_name,
        "-n",
        namespace
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

    print(describe_pods(namespace, pod))