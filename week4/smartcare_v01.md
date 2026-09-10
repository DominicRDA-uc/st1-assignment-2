# SmartCare v0.1 - Initial Engineering Brief and AI Activity Card

*A2 Case Study Stage 1 - completed by Dominic*

## SmartCare scenario

SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The client says: "We need software to help manage patients, practitioners and appointments." This is not yet a complete specification.

## Initial Engineering Brief

### 1. Problem summary

SmartCare Community Clinic currently manages patient records and appointment bookings manually, using a mix of spreadsheets and paper files. This has led to duplicate bookings, lost or hard-to-find patient records, inconsistent appointment status, and no reliable way to see practitioner availability. Cancellations are handled manually and are easy to miss, and staff cannot quickly produce basic reports on appointment activity. Management wants a simple, first-version software system to manage patients, practitioners and appointments, without the complexity of a full hospital information system. The system needs to reduce these operational problems while remaining easy for clinic staff to learn and use every day.

### 2. Initial stakeholders

| Stakeholder | Possible need |
|---|---|
| Reception / admin staff | A quick, reliable way to search patient records and book or cancel appointments without creating duplicates. |
| GPs / practitioners | Clear visibility of their own daily schedule, so they know who is booked in and when. |
| Patients | Confidence that their appointment is booked correctly and can be found again if they call to check or change it. |
| Clinic manager / owner | Basic operational reports, e.g. how many appointments were booked, completed or cancelled in a period. |
| Developer (this role) | Clear, step-by-step requirements so the system can be built iteratively without over-engineering v0.1. |

### 3. Initial features

| Feature | Confirmed or provisional? | Why? |
|---|---|---|
| Add / view patient records | Confirmed | Directly requested by the client and addresses "difficulty locating patient records." |
| Add / view practitioner records | Confirmed | Needed before appointments can be linked to a specific practitioner. |
| Book an appointment | Confirmed | Core requirement stated by the client. |
| Cancel an appointment | Confirmed | Explicitly listed as a current manual pain point. |
| Prevent double-booking a practitioner | Provisional | Clearly needed (duplicate bookings are a stated problem), but the exact rule isn't confirmed yet - see client questions below. |
| View a patient's appointment history | Confirmed | Client wants "reliable appointment history." |
| Basic operational report | Provisional | Client wants reports, but hasn't said what data they actually need in them. |
| Staff login / permissions | Provisional | Not mentioned by the client yet - unclear if multiple staff use the system at once. |

### 4. Questions for the client

1. Can a practitioner ever have two appointments at the same time (for example, a group session), or should the system always block double-booking?
2. What appointment statuses does the clinic actually need (e.g. Scheduled, Completed, Cancelled, No-show), and who is allowed to change them?
3. Will more than one staff member use the system at the same time, and if so, do we need separate logins or permission levels?
4. What exact information should the operational reports show, and how often are they needed - daily, weekly, or monthly?
5. Is it acceptable for this early prototype to store data only in memory (lost when the program closes), or is permanent storage needed from v0.1?

### 5. What we do not yet know

1. Whether the clinic operates from a single site or needs to support multiple locations or rooms.
2. How practitioner availability and working hours should be defined, entered and kept up to date.
3. What data privacy or record-keeping rules apply to patient health information stored by the system.

## AI Activity Card - Ask, Check, Explain

This section documents how I used AI as a tutor to review the SmartCare v0.1 prototype (`smartcare_v0_1.py`), following the Ask, Check, Explain process.

### Before AI

Before asking the AI anything, I read back over my own code and noted what I thought it did and where I already suspected problems: the `Clinic` class stores patients, practitioners and appointments as plain lists in memory, and the menu functions call its methods to add records and manage bookings. I already suspected two things: (1) `book_appointment()` never checks whether the chosen practitioner is already busy at that date and time, so double-booking looked possible, and (2) an earlier version of `find_patient()` compared names with `==`, which meant a search would fail unless the case matched exactly.

### AI request

Prompt used: *"Act as a tutor. Explain this code and identify potential problems. Do not provide a complete replacement. Ask me questions that help me reason about the solution."*

### Evaluate

| Suggestion | Useful | Unclear | Incorrect | Out of scope |
|---|---|---|---|---|
| Check for an existing appointment at the same date/time before booking, to stop double-booking. | ✓ | | | |
| Make `find_patient()` case-insensitive and match on part of the name, not just an exact match. | ✓ | | | |
| Make `cancel_appointment()` tell the caller whether the id was actually found, instead of failing silently. | ✓ | | | |
| Move to a database (e.g. SQLite) instead of in-memory lists so data survives a restart. | ✓ | | | ✓ |
| Add docstrings and type hints so the classes and methods are easier to read. | ✓ | | | |
| Store the next appointment id in a global variable instead of on the `Clinic` object. | | | ✓ | |
| "Add better error handling generally." | | ✓ | | |
| Rebuild the whole prototype with a graphical interface. | | | | ✓ |

### Decide

*For each significant suggestion: Accept / Modify / Reject / Keep unverified.*

- **Double-booking check** - Accept, but deferred: this is important (it maps directly onto the "duplicate appointment bookings" problem in the case study) but needs the `datetime` module to compare dates/times properly rather than as plain strings, so it is planned for v0.2 and left as a documented limitation for now.
- **Case-insensitive / partial name search** - Accept. Implemented directly in `find_patient()` in this version.
- **`cancel_appointment()` reports success/failure** - Accept. Implemented directly; the method now returns `True`/`False` and the menu prints a matching message.
- **Move to a database now** - Reject for this stage. The brief says v1 should stay simple, and Stage 1 is only meant to prove the basic patient/practitioner/appointment relationships work; storage is a good candidate for a later stage.
- **Docstrings and type hints** - Accept. Added throughout the module.
- **Global variable for the id counter** - Reject. Keeping the counter as an attribute on `Clinic` is safer and is already the more normal approach for a class-based design, so the suggestion was not followed.
- **"Add better error handling generally"** - Keep unverified. Too vague to act on without specific examples, so no change was made; I would ask a follow-up question if I used this suggestion again.
- **Rebuild with a GUI** - Reject. Out of scope for this stage; the client asked for a simple v1, and a text menu is enough to demonstrate the required behaviour.

### Verify

- Run the code - the program runs from the command line and shows the menu without errors.
- Test normal input - added one patient and one practitioner, then booked a normal appointment; it was stored and showed correctly in the patient's history and the practitioner's schedule.
- Test unusual input - deliberately booked the same practitioner twice for the same patient at the same date and time; the program accepted both bookings, confirming the double-booking gap the AI flagged is real.
- Compare with requirements - checked the Initial features table above: add/view records, booking, cancelling and history are all working; double-booking prevention and reporting detail are still outstanding.
- Ask tutor/peer - discussed the double-booking gap; agreed it should be the first thing tackled in Stage 2 since it is explicitly named as a current clinic problem.
- Check documentation - looked at the Python `datetime` module documentation, since a proper availability check will need real date/time comparisons rather than comparing strings.

### Explain

Yes - I can explain the whole program without re-reading the AI's explanation. I understand why each class exists (`Patient`, `Practitioner` and `Appointment` model the three things the clinic actually manages), how an `Appointment` links a `Patient` and a `Practitioner` together, and why the original case-sensitive search and the missing double-booking check were real problems rather than just style issues. What I still need to understand better is how to compare date and time values properly in Python (using the `datetime` module instead of comparing strings) so that the availability check I add in Stage 2 is actually reliable.
