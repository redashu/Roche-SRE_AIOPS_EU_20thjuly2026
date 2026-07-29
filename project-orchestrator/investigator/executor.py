import json
import os
import sys

# --------------------------------------------------
# Add Project Root
# --------------------------------------------------

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from ai.tools.tool_registry import execute_tool


# --------------------------------------------------
# Investigation Executor
# --------------------------------------------------

class InvestigationExecutor:

    def __init__(self):

        self.evidence = {}

    # ------------------------------------------------

    def execute(self, plan):

        self.evidence = {}

        for step in plan["investigation"]:

            tool_name = step["tool"]

            print(f"\nExecuting : {tool_name}")

            try:

                result = execute_tool(tool_name)

                self.evidence[tool_name] = {

                    "success": True,

                    "reason": step["reason"],

                    "output": result

                }

            except Exception as e:

                self.evidence[tool_name] = {

                    "success": False,

                    "reason": step["reason"],

                    "error": str(e)

                }

        return self.evidence

    # ------------------------------------------------

    def print_evidence(self):

        print("\n")
        print("=" * 70)
        print("Collected Evidence")
        print("=" * 70)

        print(
            json.dumps(
                self.evidence,
                indent=4
            )
        )


# --------------------------------------------------
# CLI Testing
# --------------------------------------------------

if __name__ == "__main__":

    sample_plan = {

        "investigation": [

            {

                "tool": "get_all_pods",

                "reason": "Check pod health"

            },

            {

                "tool": "get_cluster_events",

                "reason": "Inspect cluster events"

            }

        ]

    }

    executor = InvestigationExecutor()

    evidence = executor.execute(sample_plan)

    executor.print_evidence()