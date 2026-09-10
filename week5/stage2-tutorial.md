# Assignment 2 Case Study – Stage 2 Tutorial: From Problems to Requirements

Week 5 | 60 minutes

## Learning goals

- Analyse stakeholders.
- Distinguish functional and non-functional requirements.
- Recognise ambiguity and unsupported requirements.
- Define scope.
- Develop user stories and acceptance criteria.
- Critique AI-generated requirements.

## Activity 1 – Stakeholder Map

| Stakeholder | Need | Potential conflict |
|---|---|---|
| Patients | A quick, reliable way to have appointments booked and confirmed, with accurate records kept about them. | May want to book directly online, which could conflict with staff wanting to control and verify all bookings manually. |
| Reception/admin staff | A fast, centralised way to manage patient records and appointments instead of paper/spreadsheets. | Want simple day-to-day workflows, which could conflict with management wanting more detailed data entry for reporting. |
| Practitioners (GPs) | Accurate, up-to-date visibility of their own schedule and patient history. | May want flexibility to adjust bookings freely, which could conflict with rules designed to prevent double-booking. |
| Clinic management | Operational reports and confidence the system reduces existing problems (duplicate bookings, lost records). | May want more tracking/reporting features than is practical for a "small, maintainable" v0.2, risking scope creep. |
| Developer (this role) | Clear, evidence-based requirements and a defined scope so the system stays maintainable. | May be pushed to add AI- or stakeholder-suggested features that aren't actually confirmed by the client. |

## Activity 2 – Functional or Non-Functional?

- ☑ **Functional** — The system shall allow staff to cancel an appointment. *(an observable action the system performs)*
- ☑ **Non-functional** — The system should remain responsive for the course-scale dataset. *(a performance/quality attribute, not a specific behaviour)*
- ☑ **Functional** — The system shall retain cancelled appointments. *(a specific, observable behaviour of the system)*
- ☑ **Non-functional** — Core business logic should be independently testable. *(a quality/design attribute, about how the system is built)*
- ☑ **Functional** — The system shall search for a patient by ID. *(an observable capability)*

## Activity 3 – Repair Ambiguous Requirements

**"The system should be easy to use."**
Problem: "Easy to use" is subjective and has no measurable standard, so it can't be tested or verified.
Clarification question: What specific usability standard should be met — for example, should a new staff member be able to book an appointment within a set time with no training?

**"Patient search should be fast."**
Problem: "Fast" has no defined threshold, so there's no way to check whether it's actually met.
Clarification question: What is the maximum acceptable response time for a patient search, given the expected number of records?

**"The system should securely manage data."**
Problem: "Securely" doesn't specify what security measures or standard are actually required.
Clarification question: Are there specific security requirements — such as password protection, access levels, or compliance with a health-data privacy standard — that the system must meet?

**"Appointments should normally be easy to cancel."**
Problem: Both "normally" and "easy" are vague — it's unclear what the exceptions are or how many steps counts as "easy."
Clarification question: Are there conditions where cancellation should be restricted (e.g. same-day, already-completed appointments), and is there a maximum number of steps cancelling should take?

## Activity 4 – AI Requirements Audit

| AI suggestion | Classification | Evidence / reason |
|---|---|---|
| Patients receive SMS reminders. | Assumption requiring validation | Not mentioned by the client, but a plausible extension of appointment management — needs client confirmation before including. |
| Facial recognition login. | Unsupported / Out of scope | No client evidence at all; conflicts with the client's request for a small, maintainable system and adds privacy/complexity risk. |
| Receptionists create appointments. | Confirmed | Directly implied — staff currently manage bookings manually and report duplicate-booking problems. |
| Online payment. | Unsupported | Not mentioned anywhere in the client brief; no evidence billing is part of this system. |
| Practitioners view schedules. | Confirmed | Directly addresses the stated problem of "limited visibility of practitioner availability." |
| AI recommends treatments. | Out of scope | Clinical decision-making is outside a patient/practitioner/appointment system and carries serious liability risk. |
| Cancelled appointments remain in history. | Confirmed | Directly supports the stated problem of "lack of reliable appointment history." |

## Exit question

**Why is 'AI suggested it' not sufficient evidence for a requirement?**

Because an AI generates plausible-sounding suggestions based on patterns in its training data, not on what this specific client actually said or needs. It has no real knowledge of the clinic's constraints, priorities, or context, so treating its output as a requirement risks building features nobody asked for (scope creep) or missing what the client is genuinely asking for. A requirement needs to trace back to actual client evidence — a statement, a stated problem, or a confirmed answer to a clarification question — not just to something that sounded reasonable.
