"""
SmartCare Clinic - Domain Model Skeletons (v0.3)

Stage 3 deliverable: simple class skeletons matching the UML class
diagram in smartcare_v03.md. These define structure only - attributes
and method signatures - no behaviour is implemented yet, per the
Stage 3 Lab's Part H (Consistency Check): "do not implement full
behaviour yet." Full logic is planned for a later stage.
"""


class Patient:
    def __init__(self, patient_id, name, phone):
        self.patient_id = patient_id
        self.name = name
        self.phone = phone


class Practitioner:
    def __init__(self, practitioner_id, name, specialty):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date = date
        self.time = time
        self.status = "Scheduled"

    def cancel(self):
        """Change this appointment's status to Cancelled (FR-07/FR-08).
        Structure only for now - behaviour comes in a later stage."""
        pass


class Clinic:
    """Optional coordinating class - see Design Rationale in
    smartcare_v03.md for why this exists alongside Patient,
    Practitioner and Appointment."""

    def __init__(self):
        self.patients = []
        self.practitioners = []
        self.appointments = []

    def add_patient(self, name, phone):
        """Create and store a new Patient (FR-01). Structure only."""
        pass

    def add_practitioner(self, name, specialty):
        """Create and store a new Practitioner (FR-04). Structure only."""
        pass

    def book_appointment(self, patient, practitioner, date, time):
        """Create a new Appointment (FR-06), after checking the
        practitioner isn't already booked at that date/time (FR-11).
        Structure only - conflict-checking logic comes later."""
        pass

    def cancel_appointment(self, appointment_id):
        """Find an appointment by id and cancel it (FR-07).
        Structure only for now."""
        pass

    def status_report(self):
        """Return counts of appointments by status (FR-12).
        Structure only for now."""
        pass