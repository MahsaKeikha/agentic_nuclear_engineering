"""Fail-closed, review-only governance for F89 nuclear engineering."""

BLOCKED_ACTIONS = {
    "autonomous_operational_control",
    "bypass_qualified_review",
    "fabricate_compliance_evidence",
    "issue_control_command",
    "override_protection",
    "authorize_plant_operation",
}

REQUIRED_REVIEWS = (
    "requirements_reviewed",
    "safety_case_reviewed",
    "compliance_reviewed",
    "risk_reviewed",
    "evidence_provenance_reviewed",
    "independent_verification_reviewed",
    "change_control_reviewed",
    "qualified_human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    """Authorize analysis release only after complete qualified review."""
    context = context or {}
    if action in BLOCKED_ACTIONS:
        return {
            "allowed": False,
            "reason": "operational or safety-critical control is outside reference-system authority",
        }

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {
            "allowed": False,
            "reason": "missing required qualified review",
            "missing": missing,
        }

    blockers = []
    if context.get("unresolved_high_risk_issue"):
        blockers.append("unresolved high-risk issue")
    if context.get("safety_case_gap"):
        blockers.append("safety-case evidence incomplete")
    if context.get("compliance_gap"):
        blockers.append("compliance gap unresolved")
    if context.get("verification_gap"):
        blockers.append("independent verification incomplete")
    if context.get("evidence_provenance_missing"):
        blockers.append("evidence provenance incomplete")
    if context.get("unreviewed_change"):
        blockers.append("change-control review incomplete")

    if blockers:
        return {
            "allowed": False,
            "reason": "nuclear engineering governance blocker",
            "blockers": blockers,
        }

    return {
        "allowed": True,
        "reason": "analysis package approved after qualified human review",
    }


def check(action: str, context: dict | None = None) -> dict:
    """Backward-compatible policy entry point."""
    result = authorize(action, context)
    if not result["allowed"] and action in BLOCKED_ACTIONS:
        raise PermissionError(f"Blocked action: {action}")
    return {**result, "qualified_human_review_required": True}
