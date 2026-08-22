from orchestration.orchestrator import run
from safety.policy import authorize


def valid_context():
    return {
        "requirements_reviewed": True,
        "safety_case_reviewed": True,
        "compliance_reviewed": True,
        "risk_reviewed": True,
        "evidence_provenance_reviewed": True,
        "independent_verification_reviewed": True,
        "change_control_reviewed": True,
        "qualified_human_approval": True,
    }


def test_complete_review_can_release_analysis_package():
    result = run(valid_context())
    assert result["release_allowed"] is True
    assert result["operational_control"] is False
    assert result["autonomous_safety_authority"] is False


def test_missing_qualified_human_approval_fails_closed():
    context = valid_context()
    context["qualified_human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_operational_control_is_never_authorized():
    assert authorize("autonomous_operational_control", valid_context())["allowed"] is False


def test_unresolved_high_risk_issue_blocks_release():
    context = valid_context()
    context["unresolved_high_risk_issue"] = True
    assert run(context)["release_allowed"] is False


def test_safety_case_gap_blocks_release():
    context = valid_context()
    context["safety_case_gap"] = True
    assert run(context)["release_allowed"] is False


def test_compliance_gap_blocks_release():
    context = valid_context()
    context["compliance_gap"] = True
    assert run(context)["release_allowed"] is False


def test_verification_gap_blocks_release():
    context = valid_context()
    context["verification_gap"] = True
    assert run(context)["release_allowed"] is False


def test_unreviewed_change_blocks_release():
    context = valid_context()
    context["unreviewed_change"] = True
    assert run(context)["release_allowed"] is False
