# Assignment 2 Case Study – Stage 3 Tutorial: From Requirements to Domain Models

Week 6 | 60 minutes

## Candidate Concepts

| Candidate | Class? | Reason |
|---|---|---|
| Patient | Yes | A distinct real-world entity with its own identity, data (name, contact details) and behaviour relevant to the domain (e.g. having an appointment history). |
| Practitioner | Yes | Same reasoning as Patient — a distinct entity with its own identity, attributes (name, specialty) and its own schedule of appointments. |
| Appointment | Yes | A meaningful concept linking a Patient and a Practitioner at a specific time, with its own state (status) and behaviour (being cancelled). |
| Name | No | An attribute of Patient or Practitioner, not a standalone concept with its own identity or behaviour. |
| Clinic | No (for v0.3) | Not supported by a confirmed requirement — v0.2 doesn't mention multi-clinic or multi-location support, so treating it as a full domain class now would be over-engineering ahead of evidence. |
| Database | No | A technical/storage concern belonging to the implementation layer, not a concept from the problem domain itself. |
| Cancellation | No | A behaviour/event performed on an Appointment (a status change), not an object with its own identity. |
| Status | No | An attribute (state) of Appointment, not a class of its own. |

## CRC Cards

### Patient

| Responsibilities | Collaborators |
|---|---|
| Know its own identifying and contact details (name, phone). | — |
| Know its own appointment history. | Appointment |

### Practitioner

| Responsibilities | Collaborators |
|---|---|
| Know its own identifying details (name, specialty). | — |
| Know its own schedule of upcoming appointments. | Appointment |

### Appointment

| Responsibilities | Collaborators |
|---|---|
| Know the patient and practitioner involved, and the date/time. | Patient, Practitioner |
| Track and update its own status (e.g. Scheduled, Cancelled). | — |

## Relationship Reasoning

**Patient to Appointment: which relationship and why?**
A plain association, not composition or inheritance. One Patient can have many Appointments over time, but an Appointment doesn't belong exclusively to the Patient — it also involves a Practitioner, and v0.2's requirement to retain cancelled appointments (FR-08) means an Appointment needs to be able to outlive changes to the Patient record it's associated with, rather than being owned/destroyed by it.

**Practitioner to Appointment: what multiplicity?**
One-to-many: a Practitioner can have many Appointments (1..* on the Appointment side), but each Appointment has exactly one Practitioner (1 on the Practitioner side). The same shape as the Patient–Appointment relationship.

**Should Appointment inherit from Patient?**
No. Inheritance models an "is-a" relationship, and an Appointment is not a type of Patient — it's a separate concept that relates two different entities (a Patient and a Practitioner) at a point in time. That's exactly what association is for; inheritance here would misrepresent the relationship.

**Does Clinic need to own every object?**
No, not at this stage. Nothing in the confirmed v0.2 requirements supports multiple clinics or locations, so introducing a Clinic class that "owns" every Patient, Practitioner and Appointment isn't justified yet. The three domain classes can exist as their own top-level concepts, coordinated by ordinary application code (as the existing `Clinic` class in the prototype already does) without that being a strict ownership relationship in the domain model.

## AI Model Critique

Critique of AI-proposed classes: `PatientManager`, `PractitionerManager`, `AppointmentManager`, `ClinicController`, `NotificationManager`, `ScheduleEngine`.

- **PatientManager / PractitionerManager / AppointmentManager** — Reject as domain classes. A "manager" class for CRUD operations is an architectural pattern, not a real-world domain concept, and nothing at this stage requires that extra layer — the domain classes themselves plus the existing coordinating code are enough for v0.3.
- **ClinicController** — Modify, don't add as new. Some coordinating class is genuinely useful, but it already exists as `Clinic` in the current codebase — adding a second, differently-named one would be redundant rather than a real design improvement.
- **NotificationManager** — Reject. No confirmed requirement supports notifications yet; SMS/email reminders are still an open question in the v0.2 spec (Section 7), not a confirmed requirement, so a class for it is premature.
- **ScheduleEngine** — Reject for v0.3. Nothing in the confirmed requirements calls for scheduling logic beyond the basic double-booking check (FR-11); "engine" implies more sophistication than the current evidence supports.
