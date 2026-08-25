# Lab 2 — Agile Backlog Creation & Sprint Simulation in Jira

**Kshitij G Shettigar · PES1UG24CS240**
**Problem Statement #52 — Community Tool & Equipment Library**

The five functional and two non-functional requirements from [Lab 1](../Lab1/) were
grouped into 5 Epics, decomposed into 17 User Stories totalling 73 story points,
prioritised, estimated on the Fibonacci scale, and executed as two one-week sprints
in a company-managed Jira Scrum project.

## Deliverables

| File | Contents |
|---|---|
| `Lab-2.docx` | All five deliverables — Epics, User Stories, sprint plan, Jira evidence, reflection |
| `Lab-2.pdf` | Word export of the above |
| `Lab2_Jira_Sheet.md` | The backlog as built in Jira: every Epic and Story summary, description, priority and estimate |

Jira evidence — backlog, story points, both sprint boards, Epic completion and both
burndown charts — is embedded in `Lab-2.pdf` under *Deliverable 4*, one figure per
step of the lab.

## Epics

| Epic | Traces to Lab 1 | Stories | Points |
|---|---|---|---|
| EPIC-1 Tool Catalogue & Availability | FR-002, NFR-001 | 3 | 13 |
| EPIC-2 Reservations & Pickup Windows | FR-003 | 3 | 10 |
| EPIC-3 Borrowing & Member Eligibility | FR-004 | 3 | 13 |
| EPIC-4 Deposits, Fees & Payments | FR-001, NFR-002 | 4 | 21 |
| EPIC-5 Returns & Damage Settlement | FR-005, NFR-002 | 4 | 16 |
| **Total** | | **17** | **73** |

Every Lab 1 requirement is traced to at least one User Story.

## Sprints

Split on the Epic boundary rather than an arbitrary point, so each sprint delivers a
capability demonstrable end to end.

| Sprint | Goal | Stories | Points |
|---|---|---|---|
| **Sprint 1 — Discovery & Access** | A member can find a tool, trust the availability shown, hold it for pickup, and be correctly allowed or refused at checkout. | 9 | 36 |
| **Sprint 2 — Deposit Settlement** | Every loan is backed by a correctly calculated deposit taken through the payment gateway, and every return is settled with an itemised, auditable breakdown. | 8 | 37 |

## Estimation

Story points use the Fibonacci scale (2, 3, 5, 8). The two 8-point stories — 3.1
(verify borrowing eligibility) and 4.4 (tokenised deposit holds) — are sized high
because neither is self-contained: 3.1 reads state owned by other stories, and 4.4
depends on an external payment gateway. That dependency risk is what the scale's
non-linearity is for.

## Reflection

Answers to the four reflection questions are in `Lab-2.docx`, section
*Deliverable 5*. In short: both sprints closed at 100%, which reflects the
simulation rather than the estimates — dragging cards between columns cannot
surface a story that turns out harder than planned. The burndown is flat-then-cliff
for the same reason, and a velocity of ~36 points derived from simulated
completions is not yet evidence of capacity.
