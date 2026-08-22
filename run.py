from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "nuclear engineering review package",
    "requirements_reviewed": True,
    "safety_case_reviewed": True,
    "compliance_reviewed": True,
    "risk_reviewed": True,
    "evidence_provenance_reviewed": True,
    "independent_verification_reviewed": True,
    "change_control_reviewed": True,
    "qualified_human_approval": True,
}

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
