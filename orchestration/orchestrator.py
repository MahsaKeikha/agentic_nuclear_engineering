from AGENTS.requirements_agent import run as requirements
from AGENTS.safety_case_agent import run as safety_case
from AGENTS.compliance_agent import run as compliance
from AGENTS.risk_review_agent import run as risk_review
from AGENTS.evidence_agent import run as evidence


def run(context):
    state = {"input": context, "stages": []}
    for name, fn in [("requirements", requirements), ("safety_case", safety_case), ("compliance", compliance), ("risk_review", risk_review), ("evidence", evidence)]:
        state["stages"].append({"stage": name, "output": fn(state)})
    state["status"] = "qualified_human_review_required"
    return state
