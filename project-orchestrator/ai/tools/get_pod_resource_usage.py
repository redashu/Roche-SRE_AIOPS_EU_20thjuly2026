import json
import subprocess


def parse_cpu(cpu):
    """
    Convert Kubernetes CPU values to millicores.
    """

    if cpu.endswith("m"):
        return int(cpu[:-1])

    return int(float(cpu) * 1000)


def parse_memory(memory):
    """
    Convert Kubernetes memory values to Mi.
    """

    memory = memory.strip()

    if memory.endswith("Ki"):
        return round(float(memory[:-2]) / 1024, 2)

    if memory.endswith("Mi"):
        return float(memory[:-2])

    if memory.endswith("Gi"):
        return float(memory[:-2]) * 1024

    if memory.endswith("Ti"):
        return float(memory[:-2]) * 1024 * 1024

    return 0


def get_pod_resource_usage():

    cmd = [
        "kubectl",
        "top",
        "pods",
        "-A",
        "--no-headers"
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    cpu_sorted = []
    memory_sorted = []

    for line in result.stdout.strip().splitlines():

        cols = line.split()

        if len(cols) < 4:
            continue

        namespace = cols[0]
        pod = cols[1]
        cpu = cols[2]
        memory = cols[3]

        record = {
            "namespace": namespace,
            "pod": pod,
            "cpu": cpu,
            "memory": memory,
            "cpu_millicores": parse_cpu(cpu),
            "memory_mi": parse_memory(memory)
        }

        cpu_sorted.append(record)
        memory_sorted.append(record)

    cpu_sorted = sorted(
        cpu_sorted,
        key=lambda x: x["cpu_millicores"],
        reverse=True
    )

    memory_sorted = sorted(
        memory_sorted,
        key=lambda x: x["memory_mi"],
        reverse=True
    )

    return {
        "cpu_sorted": cpu_sorted,
        "memory_sorted": memory_sorted
    }


if __name__ == "__main__":

    print(
        json.dumps(
            get_pod_resource_usage(),
            indent=2
        )
    )