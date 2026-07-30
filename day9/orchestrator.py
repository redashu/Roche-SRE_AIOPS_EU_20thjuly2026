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
from investigator.reducer import EvidenceReducer
from investigator.router import QueryRouter

from ai.tool_result_summary import summarize

from rag.rag_chat_bedrock import BedrockRAG


# --------------------------------------------------
# Investigation Orchestrator
# --------------------------------------------------

class InvestigationOrchestrator:

    def __init__(self):

        self.router = QueryRouter()

        self.rag = BedrockRAG(

            region="ap-south-1",

            knowledge_base_id="GBM9DEBFZ5",

            model_arn=(
                "arn:aws:bedrock:ap-south-1:992382386705:"
                "application-inference-profile/c3iuy36tpgle"
            )

        )

        self.planner = InvestigationPlanner()

        self.executor = InvestigationExecutor()

        self.reducer = EvidenceReducer()

    # --------------------------------------------------
    # RAG Flow
    # --------------------------------------------------

    def handle_rag(self, question):

        print("\n")
        print("=" * 80)
        print("STEP 2 : Enterprise Knowledge Search")
        print("=" * 80)

        result = self.rag.ask(question)

        return {

            "success": True,

            "route": "RAG",

            "question": question,

            "answer": result["answer"],

            "citations": result.get("citations", [])

        }

    # --------------------------------------------------
    # LIVE Investigation Flow
    # --------------------------------------------------

    def handle_live(self, question):

        print("\n")
        print("=" * 80)
        print("STEP 2 : Creating Investigation Plan")
        print("=" * 80)

        plan = self.planner.create_plan(question)

        self.planner.print_plan(plan)

        print("\n")
        print("=" * 80)
        print("STEP 3 : Executing Investigation")
        print("=" * 80)

        evidence = self.executor.execute(plan)

        print("\n")
        print("=" * 80)
        print("STEP 4 : Evidence Collected")
        print("=" * 80)

        self.executor.print_evidence()

        print("\n")
        print("=" * 80)
        print("STEP 5 : Root Cause Analysis")
        print("=" * 80)

        reduced = self.reducer.reduce(evidence)

        self.reducer.print_reduced(reduced)

        print("\n")
        print("=" * 80)
        print("STEP 6 : Generating Final Response")
        print("=" * 80)

        answer = summarize(
            question,
            reduced
        )

        return {

            "success": True,

            "route": "LIVE",

            "question": question,

            "plan": plan,

            "evidence": evidence,

            "answer": answer

        }

    # --------------------------------------------------
    # Main Entry Point
    # --------------------------------------------------

    def investigate(self, question):

        print("\n")
        print("=" * 80)
        print("STEP 1 : Intent Routing")
        print("=" * 80)

        route = self.router.route(question)

        print(f"\nRouter Decision : {route}")

        if route == "RAG":

            return self.handle_rag(question)

        return self.handle_live(question)


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

        print(f"Route : {result['route']}")
        print()

        print(result["answer"])

        if result["route"] == "RAG" and result.get("citations"):

            print("\n")
            print("=" * 80)
            print("REFERENCES")
            print("=" * 80)

            for i, citation in enumerate(result["citations"], start=1):

                print(f"\n[{i}] {citation['document']}")