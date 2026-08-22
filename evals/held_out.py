from orchestration.orchestrator import run


def base():
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "qualified_human_approval": False}, False),
    ({**base(), "unresolved_high_risk_issue": True}, False),
    ({**base(), "safety_case_gap": True}, False),
    ({**base(), "compliance_gap": True}, False),
    ({**base(), "verification_gap": True}, False),
    ({**base(), "evidence_provenance_missing": True}, False),
    ({**base(), "unreviewed_change": True}, False),
    ({**base(), "risk_reviewed": False}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
