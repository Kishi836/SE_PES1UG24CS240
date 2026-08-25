# Lab 2 — Jira Copy-Paste Sheet

**Kshitij G Shettigar | PES1UG24CS240 | PS-52 Community Tool & Equipment Library**

Work top to bottom. Do NOT start a sprint until every Epic and Story exists with its Priority and Story Points set.

---

## STEP 1 — Create the 5 Epics

Backlog → blue **Create** button → Work type = **Epic** → paste Summary + Description → Create.

### EPIC 1
**Summary:** `EPIC-1 Tool Catalogue & Availability`

**Description:**
```
Enables Community Members to find equipment and see its true, real-time
physical availability across every neighbourhood depot locker before they
travel to collect it.

Covers Lab 1 requirements: FR-002, NFR-001.
```

### EPIC 2
**Summary:** `EPIC-2 Reservations & Pickup Windows`

**Description:**
```
Enables a Community Member to hold an available item for a bounded pickup
window, and returns uncollected items to circulation automatically so that
scarce tools are never blocked by a no-show.

Covers Lab 1 requirements: FR-003.
```

### EPIC 3
**Summary:** `EPIC-3 Borrowing & Member Eligibility`

**Description:**
```
Enforces borrowing eligibility at checkout so that members with overdue
items or unpaid fees cannot take further equipment, protecting the
high-value tools the rest of the neighbourhood is waiting on.

Covers Lab 1 requirements: FR-004.
```

### EPIC 4
**Summary:** `EPIC-4 Deposits, Fees & Payments`

**Description:**
```
Calculates security deposits from tool category, enforces loan duration
limits, accrues late fees, and processes every hold and charge through the
external payment gateway as tokenised references with no card data stored.

Covers Lab 1 requirements: FR-001, NFR-002.
```

### EPIC 5
**Summary:** `EPIC-5 Returns & Damage Settlement`

**Description:**
```
Records item condition on return, lets the Library Custodian log a damage
assessment with repair cost, and settles the held deposit with an itemised,
auditable breakdown of every deduction.

Covers Lab 1 requirements: FR-005, NFR-002.
```

---

## STEP 2 — Create the 17 User Stories

Backlog → arrow next to an Epic → **Create work item** → Work type = **Story**.

Creating from the Epic's own arrow auto-links the Story to that Epic. Use this — do not create Stories from the top Create button, or they will land unparented.

Set **Priority** in the create form. Set **Story Points** after creating: open the Story → **More fields** → Story Points.

---

### Under EPIC-1 Tool Catalogue & Availability

**Story 1.1** — Priority: **High** — Story Points: **5**

**Summary:** `Story 1.1 Search the tool catalogue`
```
As a Community Member,
I want to search the catalogue by category, keyword or date,
So that I can find the tool I need without travelling to the depot.

Acceptance: a "lawnmower" search returns only lawnmowers.
Traces to FR-002.
```

**Story 1.2** — Priority: **High** — Story Points: **5**

**Summary:** `Story 1.2 See real-time item status`
```
As a Community Member,
I want every search result to show its status (Available, Reserved, On Loan
or Under Repair),
So that I never travel for a tool that somebody else already has.

Acceptance: an item checked out 5 seconds earlier already shows On Loan.
Traces to FR-002, NFR-001.
```

**Story 1.3** — Priority: **Medium** — Story Points: **3**

**Summary:** `Story 1.3 Show depot locker location`
```
As an authenticated Community Member,
I want each available item to show its depot locker ID,
So that I can collect it from the right locker.

Acceptance: locker contents are visible only once signed in; an
unauthenticated locker request returns HTTP 401.
Traces to FR-002, NFR-001.
```

---

### Under EPIC-2 Reservations & Pickup Windows

**Story 2.1** — Priority: **High** — Story Points: **5**

**Summary:** `Story 2.1 Reserve an available item`
```
As a Community Member,
I want to reserve an available item for a pickup window of up to 24 hours,
So that it is held for me while I make my way to the depot.

Acceptance: the reservation marks the item Reserved immediately.
Traces to FR-003.
```

**Story 2.2** — Priority: **Medium** — Story Points: **3**

**Summary:** `Story 2.2 Auto-release uncollected reservations`
```
As a Library Custodian,
I want an uncollected reservation to return to Available automatically when
its pickup window closes,
So that scarce tools are not blocked by members who never turn up.

Acceptance: the item is Available within 5 minutes of the window closing.
Traces to FR-003.
```

**Story 2.3** — Priority: **Medium** — Story Points: **2**

**Summary:** `Story 2.3 Prevent double reservation`
```
As a Community Member,
I want a reserved item to be blocked from other members,
So that two of us never arrive at the depot for the same tool.

Acceptance: a second member attempting the same item is refused.
Traces to FR-003.
```

---

### Under EPIC-3 Borrowing & Member Eligibility

**Story 3.1** — Priority: **High** — Story Points: **8**

**Summary:** `Story 3.1 Verify borrowing eligibility at checkout`
```
As a Library Custodian,
I want the system to verify that a member has no overdue item and no unpaid
damage or late fee before any checkout is confirmed,
So that equipment is never lent to a member already in default.

Acceptance: checkout is refused for a member holding one overdue drill.
Traces to FR-004.
```

**Story 3.2** — Priority: **High** — Story Points: **3**

**Summary:** `Story 3.2 Block high-value items on a failed check`
```
As a Library Custodian,
I want high-value equipment blocked whenever the eligibility check fails,
So that the most costly tools stay protected from repeat defaulters.

Acceptance: a member with an overdue drill is refused a chainsaw.
Traces to FR-004.
```

**Story 3.3** — Priority: **Low** — Story Points: **2**

**Summary:** `Story 3.3 Show the refusal reason`
```
As a Community Member,
I want to be told exactly why my checkout was refused,
So that I know what to settle before I try to borrow again.

Acceptance: the refusal names the overdue item or the unpaid fee.
Traces to FR-004.
```

---

### Under EPIC-4 Deposits, Fees & Payments

**Story 4.1** — Priority: **High** — Story Points: **5**

**Summary:** `Story 4.1 Calculate deposit from tool category`
```
As a Library Custodian,
I want each item's security deposit set automatically from its tool
category,
So that the deposit held always matches the value at risk.

Acceptance: a Category-C item holds Rs.2000 at checkout.
Traces to FR-001.
```

**Story 4.2** — Priority: **High** — Story Points: **3**

**Summary:** `Story 4.2 Enforce category loan duration limits`
```
As a Library Custodian,
I want the maximum loan duration enforced per tool category,
So that high-demand equipment keeps circulating through the neighbourhood.

Acceptance: a loan longer than the 3-day Category-C limit is rejected.
Traces to FR-001.
```

**Story 4.3** — Priority: **Medium** — Story Points: **5**

**Summary:** `Story 4.3 Accrue late return fees`
```
As a Library Custodian,
I want a late fee charged for every day an item is held past its due date,
So that members have a real reason to return equipment on time.

Acceptance: a 2-day-late return is charged 2 days of late fee.
Traces to FR-001.
```

**Story 4.4** — Priority: **High** — Story Points: **8**

**Summary:** `Story 4.4 Hold deposits via tokenised payment`
```
As a Community Member,
I want my deposit held through the external payment gateway as a tokenised
reference with no card data stored,
So that my card details are never at risk from the library's systems.

Acceptance: a scan after 100 transactions finds only gateway tokens.
Traces to NFR-002.
```

---

### Under EPIC-5 Returns & Damage Settlement

**Story 5.1** — Priority: **High** — Story Points: **3**

**Summary:** `Story 5.1 Record item condition on return`
```
As a Library Custodian,
I want to record each item's condition at the moment it is returned,
So that any damage is attributed to the correct loan and member.

Acceptance: every return has a recorded condition before the loan closes.
Traces to FR-005.
```

**Story 5.2** — Priority: **High** — Story Points: **5**

**Summary:** `Story 5.2 Log a damage assessment with repair cost`
```
As a Library Custodian,
I want to log a damage assessment against a returned item with its repair
cost,
So that the cost of repair can be recovered from the held deposit.

Acceptance: a logged Rs.500 assessment is attached to that return.
Traces to FR-005.
```

**Story 5.3** — Priority: **High** — Story Points: **5**

**Summary:** `Story 5.3 Settle the deposit with an itemised breakdown`
```
As a Community Member,
I want an itemised breakdown of every deduction when my deposit is released,
So that I can see exactly what I was charged for and why.

Acceptance: Rs.500 damage and Rs.120 late fee against a Rs.2000 deposit
releases Rs.1380 with each line shown.
Traces to FR-005.
```

**Story 5.4** — Priority: **Medium** — Story Points: **3**

**Summary:** `Story 5.4 Keep an immutable settlement audit record`
```
As a Library Custodian,
I want every deposit hold, deduction and release written to an immutable
12-month audit record,
So that the library can always prove what it charged a member.

Acceptance: every deduction has a timestamped entry the application cannot
alter.
Traces to NFR-002.
```

---

## STEP 3 — Reorder the backlog by priority

Drag so High sits above Medium, and Medium above Low, within each Epic group. Story 3.3 (Low) should end up at the bottom of the Sprint 1 group.

---

## STEP 4 — Sprint 1: "Discovery & Access"

**Sprint goal** — paste into the Start Sprint dialog:
```
A member can find a tool, trust the availability shown, hold it for pickup,
and be correctly allowed or refused at checkout.
```

Tick these 9 stories and drag them into Sprint 1. **36 story points.**

| Order | Story | Priority | Points |
|---|---|---|---|
| 1 | Story 1.1 Search the tool catalogue | High | 5 |
| 2 | Story 1.2 See real-time item status | High | 5 |
| 3 | Story 2.1 Reserve an available item | High | 5 |
| 4 | Story 3.1 Verify borrowing eligibility at checkout | High | 8 |
| 5 | Story 3.2 Block high-value items on a failed check | High | 3 |
| 6 | Story 1.3 Show depot locker location | Medium | 3 |
| 7 | Story 2.2 Auto-release uncollected reservations | Medium | 3 |
| 8 | Story 2.3 Prevent double reservation | Medium | 2 |
| 9 | Story 3.3 Show the refusal reason | Low | 2 |

Start sprint → duration **1 week**.

**SCREENSHOT NOW, before moving anything:** the Backlog view with Epics and Stories visible, and the Active Sprint board with all 9 in To Do.

Then move all 9 across To Do → In Progress → Done, in the table order above. Move them in **three or four batches with a minute between**, not all at once — the burndown only draws a step where it sees a change, and one big batch gives you a single vertical drop with nothing to analyse.

**SCREENSHOT:** Active Sprint board with all 9 in Done.

Click **Complete sprint**.

---

## STEP 5 — Sprint 2: "Deposits & Settlement"

**Sprint goal:**
```
Every loan is backed by a correctly calculated deposit taken through the
payment gateway, and every return is settled with an itemised, auditable
breakdown.
```

Tick these 8 stories and drag them into Sprint 2. **37 story points.**

| Order | Story | Priority | Points |
|---|---|---|---|
| 1 | Story 4.1 Calculate deposit from tool category | High | 5 |
| 2 | Story 4.4 Hold deposits via tokenised payment | High | 8 |
| 3 | Story 4.2 Enforce category loan duration limits | High | 3 |
| 4 | Story 5.2 Log a damage assessment with repair cost | High | 5 |
| 5 | Story 5.3 Settle the deposit with an itemised breakdown | High | 5 |
| 6 | Story 5.1 Record item condition on return | High | 3 |
| 7 | Story 4.3 Accrue late return fees | Medium | 5 |
| 8 | Story 5.4 Keep an immutable settlement audit record | Medium | 3 |

Start sprint → duration **1 week**. Move all 8 to Done in batches. **Complete sprint.**

**SCREENSHOT:** the Epic panel showing completed progress bars and total points per Epic.

---

## STEP 6 — Burndown Chart

**Reports** — next to Calendar, next to Active Sprints — → **Burndown Chart**.

Switch the report to **Sprint 1**, screenshot. Switch to **Sprint 2**, screenshot.

---

## Screenshots to send me

Save them into this folder, any filename:

1. Backlog with Epics and User Stories
2. Story point assignments — Epic panel showing per-Epic totals
3. Sprint board, Active Sprint view
4. Burndown chart, Sprint 1
5. Burndown chart, Sprint 2

---

## Totals for reference

| Epic | Stories | Points |
|---|---|---|
| EPIC-1 Tool Catalogue & Availability | 3 | 13 |
| EPIC-2 Reservations & Pickup Windows | 3 | 10 |
| EPIC-3 Borrowing & Member Eligibility | 3 | 13 |
| EPIC-4 Deposits, Fees & Payments | 4 | 21 |
| EPIC-5 Returns & Damage Settlement | 4 | 16 |
| **Total** | **17** | **73** |

Sprint 1: 36 points — Sprint 2: 37 points
