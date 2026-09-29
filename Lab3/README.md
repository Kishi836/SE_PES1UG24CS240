# Lab 3 — Component Modelling & Architectural Pattern Selection

**Kshitij G Shettigar · PES1UG24CS240**
**Problem Statement #52 — Community Tool & Equipment Library**

Layered, Microservices and Client-Server styles were evaluated against the scenario;
**Layered Architecture** was selected and modelled as a UML component diagram with
provided/required (ball-and-socket) interfaces.

## Deliverables

| File | Contents |
|---|---|
| `Lab-3.png` | Deliverable 1 — UML component diagram |
| `Lab-3.pdf` | Deliverable 2 — one-page architecture justification |
| `Lab-3.docx` | Word source of the justification |
| `Lab-3.drawio` | Editable diagram source (draw.io) |

## Components

| Layer | Component | Provides | Requires |
|---|---|---|---|
| Presentation | Member Web App | — | ICatalogue, IAuth, ICheckout |
| Presentation | Custodian Console | — | ICatalogue, IReturn |
| Business | Catalogue & Reservation | ICatalogue | IRepository |
| Business | Member Account | IAuth, IEligibility | IRepository |
| Business | Loan Manager | ICheckout, IReturn | IEligibility, IPayment, IRepository |
| Business | Payment Service | IPayment | IGatewayAPI |
| Data | Library Repository | IRepository | — |
| External | Payment Gateway | IGatewayAPI | — |

Presentation-to-business interfaces are REST over HTTPS, calls inside the business
layer are in-process, the repository is reached by SQL, and the payment gateway by
HTTPS REST exchanging tokenised card references only.

## Why Layered

The loan workflow (reserve, eligibility check, deposit, return, damage settlement) is
one chain over a shared loan and deposit record, which layering keeps in one
consistent business layer; microservices would split that record across services.
The library is run by a single custodian, so one deployable unit fits better than a
fleet of services. Full reasoning, with the security and performance arguments, is in
`Lab-3.pdf`.
