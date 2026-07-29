import copy


class EvidenceReducer:

    # --------------------------------------------------
    # Main Reducer
    # --------------------------------------------------

    def reduce(self, evidence):

        reduced = {}

        for tool_name, data in evidence.items():

            output = data.get("output")

            if tool_name == "get_all_pods":

                output = self.reduce_pods(output)

            elif tool_name == "get_cluster_events":

                output = self.reduce_events(output)

            elif tool_name == "get_pod_logs":

                output = self.reduce_logs(output)

            elif tool_name == "get_pod_resource_usage":

                output = self.reduce_resource_usage(output)

            reduced[tool_name] = {
                "success": data.get("success"),
                "reason": data.get("reason"),
                "output": output
            }

        return reduced

    # --------------------------------------------------
    # Pods
    # --------------------------------------------------

    def reduce_pods(self, pods):

        if not isinstance(pods, list):
            return pods

        reduced = []

        for pod in pods:

            reduced.append({

                "namespace": pod.get("namespace"),

                "name": pod.get("name"),

                "status": pod.get("status"),

                "node": pod.get("node"),

                "pod_ip": pod.get("pod_ip"),

                "restart_count": pod.get("restart_count")

            })

        return reduced

    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def reduce_events(self, events):

        if not isinstance(events, list):
            return events

        reduced = []

        for event in events[-20:]:

            reduced.append({

                "namespace": event.get("namespace"),

                "type": event.get("type"),

                "reason": event.get("reason"),

                "object": event.get("object"),

                "message": event.get("message")

            })

        return reduced

    # --------------------------------------------------
    # Logs
    # --------------------------------------------------

    def reduce_logs(self, logs):

        if isinstance(logs, str):

            return "\n".join(
                logs.splitlines()[-50:]
            )

        return logs

    # --------------------------------------------------
    # Resource Usage
    # --------------------------------------------------

    def reduce_resource_usage(self, usage):

        if not isinstance(usage, list):
            return usage

        reduced = []

        for pod in usage:

            reduced.append({

                "namespace": pod.get("namespace"),

                "pod": pod.get("pod"),

                "cpu": pod.get("cpu"),

                "memory": pod.get("memory")

            })

        return reduced

    # --------------------------------------------------
    # Pretty Print
    # --------------------------------------------------

    def print_reduced(self, reduced):

        import json

        print("\n")
        print("=" * 80)
        print("REDUCED EVIDENCE")
        print("=" * 80)

        print(
            json.dumps(
                reduced,
                indent=4
            )
        )


# --------------------------------------------------
# CLI Test
# --------------------------------------------------

if __name__ == "__main__":

    from investigator.executor import InvestigationExecutor
    from investigator.planner import InvestigationPlanner

    planner = InvestigationPlanner()

    executor = InvestigationExecutor()

    reducer = EvidenceReducer()

    question = input("\nAsk : ")

    plan = planner.create_plan(question)

    evidence = executor.execute(plan)

    reduced = reducer.reduce(evidence)

    reducer.print_reduced(reduced)