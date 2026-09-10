# SmartCare v0.2 – Requirements Specification

*Produced following the Stage 2 Lab process: requirements drafted AI OFF, reviewed AI ON, then verified.*

## 1. Problem and Scope

SmartCare Community Clinic currently manages patients, practitioners and appointments using spreadsheets and paper records. This has resulted in duplicate bookings, difficulty locating patient information, inconsistent appointment status, and limited, unreliable appointment history. Management has asked for a small, maintainable software system to replace these manual processes for patient, practitioner and appointment records — not a full hospital information system. SmartCare v0.2 defines these requirements in more detail than the v0.1 prototype, based on evidence from the client brief and stakeholder needs, so that later stages implement a system that actually matches what the clinic needs rather than an assumed version of it.

**In scope:**
- Managing patient records (add, view, search)
- Managing practitioner records (add, view)
- Booking, viewing and cancelling appointments
- Retaining appointment history, including cancelled appointments
- Basic operational reporting on appointment status

**Out of scope (for v0.2):**
- Online/patient self-service booking — not requested by the client
- Payment or billing processing
- Facial recognition or biometric login
- AI-generated treatment or diagnosis recommendations
- Integration with external systems (e.g. insurance)

**Provisional (not yet confirmed):** SMS/email appointment reminders — plausible but not mentioned by the client; see Section 7.

## 2. Stakeholders

| Stakeholder | Need | Evidence |
|---|---|---|
| Patients | Confidence that their appointment is booked correctly and can be found again if checked. | Client brief: "difficulty finding patient information." |
| Reception/admin staff | A fast, reliable way to manage bookings without creating duplicates. | Client brief: "duplicate bookings," management wants staff to "manage patients, practitioners and appointments." |
| Practitioners (GPs) | Accurate visibility of their own schedule and patient history. | Client brief: "limited appointment history"; practitioner scheduling implied by "appointment system." |
| Clinic management | Operational reports and confidence the system reduces existing problems. | Client brief: management wants "a small, maintainable" system to fix duplicate bookings and inconsistent status. |
| Developer (this role) | Clear, evidence-based requirements within a defined, manageable scope. | Assignment brief: system built iteratively, avoiding over-engineering. |

## 3. Functional Requirements

- **FR-01:** The system shall allow staff to add a new patient record (name and contact details).
- **FR-02:** The system shall allow staff to view a list of all patient records.
- **FR-03:** The system shall allow staff to search for a patient by name, matching partial and case-insensitive input.
- **FR-04:** The system shall allow staff to add a new practitioner record (name and specialty).
- **FR-05:** The system shall allow staff to view a list of all practitioner records.
- **FR-06:** The system shall allow staff to book an appointment for a patient with a practitioner, recording a date and time.
- **FR-07:** The system shall allow staff to cancel an existing appointment.
- **FR-08:** The system shall retain cancelled appointments in the appointment history rather than deleting them.
- **FR-09:** The system shall allow staff to view a patient's appointment history.
- **FR-10:** The system shall allow staff to view a practitioner's schedule of upcoming appointments.
- **FR-11:** The system shall prevent a practitioner from being booked for two appointments at the same date and time.
- **FR-12:** The system shall allow staff to generate a report showing the number of appointments by status (e.g. Scheduled, Cancelled).

## 4. Non-Functional Requirements

- **NFR-01:** The system shall respond to user actions within approximately one second when working with a course-scale dataset (up to a few hundred records).
- **NFR-02:** Core business logic (patient, practitioner and appointment operations) shall be separated from the user interface so it can be tested independently.
- **NFR-03:** The system shall be usable by clinic staff with no programming experience, through a straightforward menu-driven interface.
- **NFR-04:** The system shall not lose or overwrite existing patient, practitioner or appointment data during normal operation.
- **NFR-05:** The codebase shall remain small and maintainable, avoiding complexity not required by a confirmed feature.
- **NFR-06:** Error messages (e.g. an invalid ID) shall be clear enough for non-technical staff to understand and act on without support.

## 5. User Stories

- **US-01:** As a receptionist, I want to add a new patient record, so that I can register new patients quickly without paper forms.
- **US-02:** As a receptionist, I want to search for a patient by name, so that I can find their record quickly during a phone call.
- **US-03:** As a receptionist, I want to book an appointment for a patient with a practitioner, so that appointments are recorded accurately instead of on paper.
- **US-04:** As a receptionist, I want to cancel an appointment, so that a freed-up slot is clearly reflected instead of causing confusion.
- **US-05:** As a practitioner, I want to view my upcoming schedule, so that I know which patients I'm seeing and when.
- **US-06:** As a clinic manager, I want to see a report of appointment counts by status, so that I can understand how the clinic is operating.

## 6. Acceptance Criteria

**AC-1 (linked to US-03/FR-06 — positive):**
GIVEN a patient and a practitioner both already exist in the system
WHEN a staff member books an appointment for that patient with that practitioner at a time the practitioner is free
THEN the appointment is created with status "Scheduled" and appears in both the patient's history and the practitioner's schedule

**AC-2 (linked to US-04/FR-07/FR-08 — positive):**
GIVEN an existing scheduled appointment
WHEN a staff member cancels that appointment using its ID
THEN the appointment's status changes to "Cancelled" and it remains visible in the patient's history rather than being deleted

**AC-3 (linked to FR-11 — negative/failure scenario):**
GIVEN a practitioner already has an appointment booked at a specific date and time
WHEN a staff member attempts to book another appointment for that same practitioner at the same date and time
THEN the system rejects the booking and displays a message explaining that the practitioner is already booked at that time

## 7. Assumptions and Open Questions

**Assumptions:**
- The clinic operates from a single site (not yet confirmed with the client).
- Only clinic staff, not patients, will use the system directly in v0.2 — no patient self-service.
- The system is used by staff on a shared computer; separate staff logins/permissions are not required yet.

**Open questions:**
- Should the system support multiple practitioners with the same specialty, and does that change scheduling rules?
- What exact information should appear on the operational report, and how often is it needed?
- Should patients receive SMS or email appointment reminders, and if so, through what channel?
- Are there confirmed data-privacy or record-keeping requirements that need to be reflected in the non-functional requirements?

## 8. AI Requirements Review Record

**Prompt used:** *"Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation."*

| AI suggestion | Evidence? | Decision | Reason | Verification |
|---|---|---|---|---|
| FR-03 didn't originally specify whether patient search matches partial or exact names — ambiguous and untestable as written. | Evidence-based (found in the requirement's own wording) | Accepted | Genuine testability gap; resolved by specifying "partial and case-insensitive" directly in FR-03, matching how search already behaves in the v0.1 prototype. | Reread FR-03 and compared it against `find_patient()` in `smartcare_v01.py`. |
| FR-12's "basic report" didn't state what data it must contain. | Evidence-based | Accepted | Untestable as originally written; FR-12 now names the exact contents (counts by appointment status). | Reread FR-12 to confirm it names specific report contents. |
| NFR-01's response time didn't state what dataset size it applied to. | Evidence-based | Modified | Fair point — added "course-scale dataset (up to a few hundred records)" so the requirement is actually testable. | Reread NFR-01 wording. |
| Suggested adding a requirement for general input validation (e.g. rejecting empty patient names). | Assumption requiring validation | Kept unverified | Reasonable idea, but the client brief doesn't mention data-entry errors specifically — needs a clarification question before becoming a firm requirement. | Logged as an open question in Section 7 rather than added as an FR. |
| Suggested adding multi-user login and permissions. | Not evidence-based | Rejected | No client evidence supports this; the brief never mentions multiple simultaneous users, and this was already rejected for the same reason during v0.1. | Cross-checked against the client brief and the v0.1 AI Activity Card decision. |
| Suggested adding SMS/email reminders as a firm requirement. | Not evidence-based / assumption | Rejected as a requirement, kept as open question | Not mentioned anywhere in the client brief. | Checked against client brief — no mention of reminders; logged in Section 7. |

## Reflection

Running the AI review after drafting the requirements myself caught two genuine gaps I'd missed: FR-03 didn't specify whether patient search should match partial or exact names, and NFR-01's response-time requirement didn't state what dataset size it applied to — both made the requirements effectively untestable as originally written. I accepted both fixes because they tightened existing requirements using evidence I'd already established (the v0.1 prototype's actual search behaviour, and the "course-scale dataset" language used elsewhere in the brief), rather than inventing anything new.

Where the AI overreached was suggesting multi-user logins/permissions and SMS reminders as new firm requirements. Neither is supported by the client brief — the clinic hasn't said multiple staff need simultaneous access, and reminders were never mentioned. Both were rejected as requirements and logged instead as open questions for the client, which felt like the more honest way to handle a plausible but unconfirmed idea rather than quietly building it in.

FR-12's "basic report" wording is the clearest example of a requirement that actually changed after review — it went from a vague reference to "a report" to a specific, testable statement of what the report must contain.

Requirements need evidence because a requirement without it is really just a guess about what the client wants. Building to a guess risks wasted work if it turns out wrong, and without a clear, sourced statement of what "correct" looks like, there's no real way to check whether the finished system actually meets the client's needs.
