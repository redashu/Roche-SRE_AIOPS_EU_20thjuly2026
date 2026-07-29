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

# --------------------------------------------------
# Imports
# --------------------------------------------------

from investigator.planner import InvestigationPlanner
from investigator.executor import InvestigationExecutor
from ai.tool_result_summary import summarize
from investigator.reducer import EvidenceReducer


# --------------------------------------------------
# Investigation Orchestrator
# --------------------------------------------------

class InvestigationOrchestrator:

    def __init__(self):

        self.planner = InvestigationPlanner()

        self.executor = InvestigationExecutor()
        self.reducer = EvidenceReducer()

    # ------------------------------------------------

    def investigate(self, question):

        print("\n")
        print("=" * 80)
        print("STEP 1 : Creating Investigation Plan")
        print("=" * 80)

        plan = self.planner.create_plan(question)

        self.planner.print_plan(plan)

        print("\n")
        print("=" * 80)
        print("STEP 2 : Executing Investigation")
        print("=" * 80)

        evidence = self.executor.execute(plan)

        print("\n")
        print("=" * 80)
        print("STEP 3 : Evidence Collected")
        print("=" * 80)

        self.executor.print_evidence()

        print("\n")
        print("=" * 80)
        print("STEP 4 : Root Cause Analysis")
        print("=" * 80)
        reduced = self.reducer.reduce(evidence)
        self.reducer.print_reduced(reduced)

        answer = summarize(
            question,
            reduced
        )

        return {

            "success": True,

            "question": question,

            "plan": plan,

            "evidence": evidence,

            "answer": answer

        }


# --------------------------------------------------
# CLI
# --------------------------------------------------

if __name__ == "__main__":

    orchestrator = InvestigationOrchestrator()

    while True:

        question = input("\nAsk : ").strip()

        if question.lower() == "exit":
            break

        result = orchestrator.investigate(question)

        print("\n")
        print("=" * 80)
        print("FINAL ANSWER")
        print("=" * 80)

        print(result["answer"])