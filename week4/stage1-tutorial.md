# Stage 1 Tutorial Activity – Why Software Engineering Still Matters

Stage 1 | Introducing Software Technology Case Study with Python and Guided AI Use

## Learning goals

- Explain why software engineering is broader than coding.
- Identify stakeholders in a simple software problem.
- Recognise missing requirements.
- Critically evaluate AI-generated feature suggestions.
- Explain why AI output should not automatically be treated as correct.

## Activity 1 – Think-Pair-Share (10 minutes)

**If ChatGPT or Copilot can produce a 100-line Python application very quickly, what knowledge does a software engineer still need?**

1. How to gather and clarify requirements from stakeholders — AI can't ask a client the right follow-up questions or spot what they forgot to mention.
2. System design judgement — decisions about architecture, scalability, security, and how a piece of software fits into a bigger system over time.
3. The ability to test, review, and critically evaluate code (including AI-generated code) for correctness, edge cases, and maintainability before trusting it.

## Activity 2 – Is This Software Engineering? (10 minutes)

| Scenario | Programming? | Software engineering? | Why? |
|---|---|---|---|
| A | Yes | No | It's a single person writing a short script with no requirements process, no stakeholders, and no ongoing maintenance — just programming. |
| B | Yes | Yes | It involves a team, real stakeholders (5,000 employees), requirements gathering, testing, and long-term maintenance at scale — the full engineering lifecycle. |
| C | Yes | No | The AI generated code from one prompt with no requirements elicitation, stakeholder input, design process, or testing — output, not engineering. |

## Activity 3 – SmartCare Problem Analysis (20 minutes)

**Client statement:** SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The clinic wants new software to improve these processes.

### Task 1 – Identify stakeholders

| Stakeholder | What do they need? |
|---|---|
| Patients | An easy, reliable way to book and check appointments, and confidence that their personal/medical information is accurate and kept private. |
| Reception/admin staff | A fast, centralised way to schedule appointments and manage records without duplicate paperwork or lost files. |
| Doctors/practitioners | Quick, accurate access to patient history and their own schedule during consultations. |
| Clinic management | Reporting and oversight to run the clinic efficiently, control costs, and stay compliant with health record regulations. |

### Task 2 – Identify current problems

1. Paper records and spreadsheets can be lost, damaged, or duplicated, with no backup.
2. There's no central system, so information isn't easily shared between staff or locations.
3. Manual scheduling increases the risk of double-booking or missed appointments.
4. Looking up a patient's history is slow, which matters during time-sensitive appointments.

### Task 3 – Ask client questions

1. How many patients and staff will use the system, and does it need to support more than one clinic location?
2. What patient data needs to be stored, and are there specific privacy or health-record regulations we need to comply with?
3. Should patients be able to book appointments themselves online, or will staff manage all bookings?
4. Are there any existing systems (billing, insurance, etc.) that the new software needs to integrate with?
5. What is the budget and timeline for this project?

## Activity 4 – Critique an AI Response (15 minutes)

**AI suggested:** appointment management; facial-recognition login; AI diagnosis recommendations; patient search; online payment; practitioner schedule view; insurance processing; automatic treatment-plan generation.

| Suggestion | Client evidence? | In scope? | Decision |
|---|---|---|---|
| Appointment management | Yes – directly stated | In scope | Include |
| Facial recognition login | No | Out of scope | Exclude — adds privacy/complexity risk with no client request |
| AI diagnosis recommendations | No | Out of scope | Exclude — clinical decision-making, major liability risk |
| Patient search | Yes – implied by "manage patients" | In scope | Include |
| Online payment | No | Unclear | Exclude for now — ask the client if billing is needed |
| Practitioner schedule view | Yes – implied by appointment management | In scope | Include |
| Insurance processing | No | Out of scope | Exclude — not mentioned, adds significant complexity |
| Treatment-plan generation | No | Out of scope | Exclude — clinical judgement, liability risk |

## Exit question

**Write one activity that a software engineer must perform and that cannot safely be delegated entirely to AI.**

Gathering and validating requirements directly with stakeholders. Understanding the clinic's real priorities, constraints, and regulatory obligations (like patient privacy) requires human judgement and conversation — an AI can't reliably infer what a client actually needs just from a short statement, and getting this wrong early on leads to building the wrong system.
