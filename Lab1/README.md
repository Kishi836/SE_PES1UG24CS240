# Lab 1 — Requirements Engineering

**Kshitij G Shettigar** · PES1UG24CS240
**Problem Statement #52 — Community Tool & Equipment Library**

## Deliverables

| # | Deliverable | File |
|---|-------------|------|
| 1 | 5 Functional + 2 Non-Functional Requirements | [`Lab-1.docx`](Lab-1.docx) / [`Lab-1.pdf`](Lab-1.pdf) |
| 2 | UML Use-Case Diagram (draw.io) | [`UseCase_Diagram.pdf`](UseCase_Diagram.pdf) · [`Use-case-diagram.png`](Use-case-diagram.png) · source: [`Lab-1.drawio`](Lab-1.drawio) |
| 3 | Use-Case Specification (UC-03 Borrow Equipment) | [`Lab-1.docx`](Lab-1.docx) / [`Lab-1.pdf`](Lab-1.pdf) |

All three deliverables are also present together in `Lab-1.docx`.

## Use-case diagram at a glance

**Actors:** Community Member · Library Custodian · Payment Gateway
**System boundary:** Community Tool & Equipment Library

| ID | Use case |
|----|----------|
| UC-01 | Search Equipment Availability |
| UC-02 | Reserve Equipment |
| UC-03 | Borrow Equipment |
| UC-04 | Return Equipment |
| UC-05 | Process Security Deposit |
| UC-06 | Log Damage Assessment |
| UC-07 | Charge Late Return Fee |

**Relationships**

- `«include»` UC-03 Borrow Equipment -> UC-05 Process Security Deposit
- `«extend»`  UC-06 Log Damage Assessment -> UC-04 Return Equipment
- `«extend»`  UC-07 Charge Late Return Fee -> UC-04 Return Equipment

## Requirements covered

| Req ID | Type | Summary |
|--------|------|---------|
| FR-001 | Functional | Calculate security deposit and loan-duration limit from tool category |
| FR-002 | Functional | Search the equipment catalogue by category, keyword and availability |
| FR-003 | Functional | Reserve an available item for a pickup window |
| FR-004 | Functional | Verify borrower eligibility before confirming checkout |
| FR-005 | Functional | Record return condition and settle the deposit |
| NFR-001 | Non-functional | Real-time availability, p95 search latency <= 2 s at 200 concurrent users |
| NFR-002 | Non-functional | All payments tokenised through the external gateway; no card data stored |

## Notes

The diagram source is `Lab-1.drawio`, editable at <https://app.diagrams.net>
(File > Open From > Device).
