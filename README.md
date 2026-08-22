# F89 | Agentic Nuclear Engineering | L3 Gold Standard | v1.0

A governed, review-only multi-agent reference system for nuclear engineering requirements, safety-case review, compliance, risk review, evidence provenance, and qualified human approval.

## Review pipeline

- Requirements review
- Safety-case review
- Compliance review
- Risk review
- Evidence review

## Gold-standard governance

F89 is fail closed. Analysis release requires reviewed requirements, safety case, compliance, risk, evidence provenance, independent verification, change control, and explicit qualified human approval.

Release is blocked for unresolved high-risk issues, safety-case gaps, compliance gaps, incomplete independent verification, missing evidence provenance, or unreviewed changes.

The reference system is review-only. It cannot issue control commands, operate facilities, override protection systems, authorize plant operation, bypass qualified review, fabricate compliance evidence, or exercise autonomous safety authority.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out review-safety suite.
