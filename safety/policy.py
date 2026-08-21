PROHIBITED = {"autonomous_operational_control", "bypass_qualified_review", "fabricate_compliance_evidence"}


def check(action):
    if action in PROHIBITED:
        raise PermissionError(f"Blocked action: {action}")
    return {"allowed": True, "qualified_human_review_required": True}
