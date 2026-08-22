from AGENTS.compliance_agent import run as compliance
from AGENTS.evidence_agent import run as evidence
from AGENTS.requirements_agent import run as requirements
from AGENTS.risk_review_agent import run as risk_review
from AGENTS.safety_case_agent import run as safety_case
from safety.policy import authorize


def run(context: dict) -> dict:
    """Run the review pipeline and apply fail-closed governance."""
    state = {"system": "F89", "input": context, "stages": []}
    for name, fn in [
        ("requirements", requirements),
        ("safety_case", safety_case),
        ("compliance", compliance),
        ("risk_review", risk_review),
        ("evidence", evidence),
    ]:
        state["stages"].append({"stage": name, "output": fn(state)})

    governance = authorize("analysis_release", context)
    state.update(
        {
            "status": "qualified_human_review_required",
            "human_review_required": True,
            "qualified_human_review_required": True,
            "governance": governance,
            "release_allowed": governance["allowed"],
            "operational_control": False,
            "autonomous_safety_authority": False,
        }
    )
    return state
