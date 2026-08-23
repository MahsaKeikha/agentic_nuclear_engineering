# F89 Agentic Nuclear Engineering

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed, review-only five-agent reference architecture for nuclear-engineering requirements, safety-case review, compliance mapping, risk review, evidence provenance, independent verification, change control, and qualified human approval.

F89 is designed as a reusable reference for structuring nuclear-engineering review workflows without granting the system operational authority. It organizes requirements, assumptions, safety claims, compliance obligations, evidence, residual risk, verification status, and reviewer decisions so critical engineering conclusions remain traceable and auditable.

This repository is intentionally review-only. It does not control equipment, operate facilities, modify protection systems, authorize plant operation, provide executable operating instructions, bypass qualified review, or replace licensed and otherwise authorized nuclear professionals.

## Review lifecycle

```text
requirements
     |
     v
safety-case review
     |
     v
compliance mapping
     |
     v
risk review
     |
     v
evidence + verification
     |
     v
qualified human approval
```

The workflow is fail closed. Safety-case gaps, unresolved high-risk findings, incomplete verification, missing evidence provenance, requirement conflicts, compliance gaps, unknown configuration state, or unreviewed changes remain blockers.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Requirements Agent | Reviews engineering, safety, interface, lifecycle, quality, and governance requirements | Are applicable requirements complete, consistent, traceable, and assigned? |
| Safety Case Agent | Reviews claims, arguments, assumptions, defense in depth, and supporting evidence | Is the safety argument explicit, evidence-backed, and appropriately bounded? |
| Compliance Agent | Maps applicable obligations, standards, commitments, and evidence | Is there traceable evidence for the compliance obligations relevant to the review context? |
| Risk Review Agent | Reviews hazards, risk significance, controls, residual risk, and unresolved issues | Are material risks identified, controlled, independently reviewed, and escalated when unresolved? |
| Evidence Agent | Reviews provenance, verification, independence, change control, and release readiness | Can each material conclusion be traced to appropriate evidence and reviewer authority? |

No specialist agent independently approves a nuclear design, facility, procedure, modification, or operational decision.

## Repository structure

```text
AGENTS/
├── requirements_agent.py
├── safety_case_agent.py
├── compliance_agent.py
├── risk_review_agent.py
└── evidence_agent.py

SKILLS/
├── requirements_traceability.py
├── safety_case_reasoning.py
├── regulatory_mapping.py
├── evidence_discipline.py
└── human_approval.py

TOOLS/
├── requirements_register.py
├── risk_register.py
├── evidence_register.py
├── assumption_tracker.py
└── review_gate.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The architecture separates specialist reasoning from deterministic registers, workflow state, safety controls, evaluation, observability, and final human authority.

## Requirements engineering

`TOOLS/requirements_register.py` provides deterministic support for requirement records. A requirement record can include source, requirement text, category, applicability, owner, verification method, verification status, evidence reference, change state, and review state.

`SKILLS/requirements_traceability.py` supports the chain:

```text
source obligation
      |
      v
system requirement
      |
      v
derived requirement
      |
      v
design response
      |
      v
verification evidence
      |
      v
review disposition
```

A requirement is not closed merely because a document references it. Closure requires appropriate evidence and review status.

## Assumption management

`TOOLS/assumption_tracker.py` records assumptions that affect the safety argument or engineering conclusion. Examples include system boundaries, environmental conditions, equipment availability, credited controls, data validity, model applicability, interface states, configuration state, verification status, and human actions.

Safety-significant assumptions must remain visible and linked to evidence where possible.

## Safety-case structure

`SKILLS/safety_case_reasoning.py` supports review of claims and supporting arguments.

```text
claim
  |
  v
argument
  |
  +--> evidence
  +--> assumptions
  +--> limitations
  +--> independent review
```

A safety claim should identify what is being claimed, the applicable system boundary and configuration, assumptions, supporting analysis, test evidence, uncertainty, limitations, and review status.

## Defense in depth and independence

The review can examine whether credited layers of prevention, protection, mitigation, monitoring, procedures, quality assurance, and emergency preparedness are identified and supported by evidence.

Redundancy is not equivalent to independence. Apparently separate protections may share power, communications, sensors, software, environment, support systems, maintenance dependencies, human actions, or physical location. Common dependencies should remain visible in the risk argument.

## Risk review

`TOOLS/risk_register.py` provides structured risk records covering the hazard or issue, cause, consequence, credited controls, risk significance, verification reference, residual risk, owner, independent review, and status.

The workflow preserves uncertainty and unresolved issues rather than compressing them into a single score.

F89 can organize deterministic analyses, probabilistic risk assessments, reliability studies, testing, inspections, operating experience, and engineering judgment. These evidence types answer different questions and should not be treated as interchangeable.

## Verification and validation

Verification asks whether an implementation satisfies specified requirements. Validation asks whether the system, model, or process is suitable for its intended use.

Review evidence can include analysis, inspection, testing, simulation, independent calculation, software verification, document review, and configuration checks. The verification method should match the significance and nature of the requirement.

Independent verification must be explicitly tracked where required. The system must not fabricate independence or infer it solely from a different reviewer name.

## Evidence provenance

`TOOLS/evidence_register.py` supports evidence records with source, version, configuration, requirement links, claim links, reviewer, review date, independence status, limitations, and approval state.

Material conclusions should be traceable to controlled evidence rather than undocumented statements.

## Configuration and change control

A safety conclusion is meaningful only for a defined configuration. Review should identify relevant document revisions, software versions, equipment revisions, analysis versions, test configurations, and operating assumption sets.

Changes can invalidate prior analysis, testing, assumptions, interfaces, or approvals. Unreviewed change is therefore a release blocker.

A change-impact review can identify affected requirements, safety claims, analyses, tests, interfaces, procedures, required re-verification, and required reapproval.

## Digital systems and cybersecurity boundary

Digital systems introduce software, timing, cybersecurity, common-cause, interface, configuration, and verification concerns. F89 can review requirements and evidence but does not modify safety-system software or protection settings.

The repository must remain separated from operational technology. It must not access plant controls, change security configurations, modify protection logic, provide bypass instructions, disable monitoring, or execute remote actions.

## Human factors and procedures boundary

Review can identify dependencies on operator recognition, response time, communication, staffing, accessibility of controls, procedure availability, training, workload, and environmental conditions.

F89 does not replace human-factors engineering or licensed operator judgment and must not generate executable plant-specific operating procedures, emergency operating steps, bypass sequences, or switching instructions.

## Quality assurance and operating experience

Safety-significant evidence may depend on controlled quality processes. Review can consider document control, records control, calibration, supplier evidence, inspection records, test records, corrective actions, nonconformance handling, and audit findings.

Operating experience can also provide evidence about failure modes, maintenance issues, human factors, common causes, and corrective actions. Its source, applicability, configuration, and disposition should remain explicit.

## Compliance mapping

`SKILLS/regulatory_mapping.py` supports traceable mapping of obligations to evidence. Applicability can vary by jurisdiction, facility type, lifecycle stage, technology, license basis, and activity.

F89 organizes compliance evidence but does not determine legal or regulatory compliance and must never fabricate approvals, licenses, regulator acceptance, inspection outcomes, certifications, exemptions, or commitments.

## Residual risk and uncertainty

Controls do not eliminate all risk. The review should identify the original concern, credited controls, evidence supporting those controls, remaining uncertainty, residual risk, owner, and acceptance authority.

Material uncertainty can arise from model assumptions, incomplete data, parameter uncertainty, measurement error, equipment reliability, human performance, external hazards, configuration uncertainty, and common-cause dependencies.

The system does not autonomously accept nuclear safety risk.

## Sensitive information boundaries

Nuclear information may be controlled, security-relevant, proprietary, export-controlled, or otherwise restricted. Implementations should enforce appropriate classification, access control, retention, and disclosure rules.

This public reference architecture should use synthetic or appropriately releasable examples and must not provide tactical facility-security instructions, vulnerability exploitation guidance, access bypasses, detailed security-response procedures, or other sensitive operational material.

## Observability

The `observability/` layer records workflow events for audit and debugging. Useful review telemetry includes requirements registered, traceability gaps, assumptions added, safety claims reviewed, evidence references, risk findings, compliance gaps, independent-verification state, change-control state, review-gate state, and human-approval state.

Observability supports auditability. It does not constitute nuclear safety evidence on its own.

## Fail-closed governance

`TOOLS/review_gate.py` provides the final release gate.

Reference blockers include:

- incomplete requirements
- unresolved requirement conflict
- traceability gaps
- incomplete safety case
- unsupported material assumptions
- unresolved high-risk issues
- unresolved compliance gaps
- missing evidence provenance
- incomplete independent verification
- unknown configuration
- unreviewed change
- incomplete required quality evidence
- unsupported operational claims
- requested control action
- requested protection override
- requested plant-operation authorization
- missing qualified human approval

Human approval is required after automated gates pass. Human approval does not convert missing evidence or unresolved safety issues into completed verification.

## Human authority boundaries

F89 must not autonomously:

- operate a nuclear facility
- issue control commands
- change setpoints
- operate plant equipment
- modify protection logic
- override interlocks or protection systems
- disable safing functions
- authorize startup, shutdown, power operation, testing, or maintenance
- create executable emergency or operating procedures
- approve safety analyses or license-basis changes
- determine regulatory compliance
- accept nuclear safety risk
- fabricate regulator or independent-review approval

Final authority remains with properly qualified and authorized nuclear engineers, operators, safety professionals, quality personnel, licensing professionals, regulators, and responsible organizations.

## End-to-end reference workflow

1. Define the review boundary, configuration, lifecycle stage, and authority limits.
2. Register applicable requirements and source provenance.
3. Build requirements-to-evidence traceability.
4. Register material assumptions.
5. Structure safety claims and supporting arguments.
6. Review defense in depth and dependency assumptions.
7. Register hazards and unresolved risks.
8. Map applicable compliance obligations to evidence.
9. Review verification and validation evidence.
10. Confirm required independent review.
11. Confirm configuration and change-control status.
12. Review evidence provenance and quality status.
13. Preserve unresolved uncertainty and findings.
14. Apply the fail-closed release gate.
15. Require qualified human approval before release.

## Evaluation and held-out governance suite

The repository includes evaluation logic under `evals/` and benchmark cases under `benchmarks/`. Evaluation should test requirement completeness, traceability enforcement, safety-case completeness, assumption visibility, high-risk escalation, compliance-gap detection, evidence provenance, independent verification, configuration control, change control, operational-authority boundaries, and human approval.

The held-out suite should include incomplete evidence, conflicting requirements, unreviewed modifications, unsupported safety claims, and requests for prohibited operational authority.

## Failure states

```text
REQUIREMENTS INCOMPLETE
REQUIREMENT CONFLICT UNRESOLVED
TRACEABILITY GAP
SAFETY CASE INCOMPLETE
ASSUMPTION UNSUPPORTED
HIGH RISK UNRESOLVED
COMPLIANCE GAP
EVIDENCE PROVENANCE MISSING
INDEPENDENT VERIFICATION REQUIRED
CONFIGURATION UNKNOWN
CHANGE REVIEW REQUIRED
QUALITY EVIDENCE INCOMPLETE
OPERATIONAL CLAIM UNSUPPORTED
CONTROL AUTHORITY PROHIBITED
PROTECTION OVERRIDE PROHIBITED
PLANT OPERATION AUTHORIZATION PROHIBITED
HUMAN APPROVAL REQUIRED
```

The system should never fabricate requirements closure, safety evidence, compliance evidence, independent verification, regulator acceptance, configuration status, risk acceptance, or human approval.

## Reproduce the reference implementation

```bash
python -m pip install -e '.[dev]'
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11, and 3.12.

## Reproducibility and review records

A reproducible review should preserve the review scope, configuration, requirements revision, assumption set, safety-case revision, risk-register revision, compliance mapping, evidence versions, verification status, independent-review state, change-control state, findings, and reviewer decisions.

## L3 Gold Standard

F89 follows the library's L3 Gold Standard structure through five specialist agents, deterministic review registers, explicit orchestration and state, safety boundaries, observability, held-out governance evaluation, CI, fail-closed release gates, and mandatory qualified human approval.

This maturity designation describes the engineering and governance structure of the repository. It is not a license, regulator approval, facility authorization, safety certification, or evidence that a nuclear system is safe to operate.

## Extending F89

Common extensions include controlled requirements systems, document-management systems, configuration-management platforms, quality-record systems, risk registers, issue trackers, verification databases, change-control workflows, regulator-commitment trackers, and audit systems.

New integrations should preserve least privilege, provenance, configuration control, information classification, cybersecurity boundaries, and qualified human authority.

## Design principles

1. Treat nuclear engineering as a requirements, evidence, configuration, and review discipline.
2. Preserve traceability from source obligation to verification evidence.
3. Make safety claims, assumptions, limitations, and independent review explicit.
4. Distinguish redundancy from true independence and expose common dependencies.
5. Keep configuration and change control attached to every safety conclusion.
6. Never infer compliance, regulator acceptance, or risk acceptance without evidence.
7. Fail closed on unresolved high-significance findings and missing verification.
8. Keep sensitive nuclear and security information within authorized controls.
9. Maintain a hard separation from operational technology and executable procedures.
10. Keep final safety, licensing, operational, and regulatory authority with qualified humans.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted, and extended subject to its license terms.

## Responsible use

Use F89 as a nuclear-engineering review and multi-agent governance reference. Validate all requirements, safety arguments, evidence, risk assumptions, configuration, quality, compliance, and verification status against the actual authorized program before relying on results.