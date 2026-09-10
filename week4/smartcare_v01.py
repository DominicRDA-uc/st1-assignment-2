"""
SmartCare Clinic - Appointment Booking System (v0.1 prototype)

Simple in-memory prototype for Stage 1 - no database yet, all data is
lost when the program closes.

Known limitation (see Stage 1 AI Activity Card): book_appointment()
does not check whether the practitioner is already busy at that
date/time, so double-booking is currently possible. Planned fix for
v0.2 once dates/times are compared properly with the datetime module.
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


class Clinic:
    """Holds all records and the operations the case study asked for."""

    def __init__(self):
        self.patients = []
        self.practitioners = []
        self.appointments = []
        self.next_id = 1  # one shared counter, kept simple for v0.1

    def add_patient(self, name, phone):
        patient = Patient(self.next_id, name, phone)
        self.patients.append(patient)
        self.next_id += 1
        return patient

    def add_practitioner(self, name, specialty):
        practitioner = Practitioner(self.next_id, name, specialty)
        self.practitioners.append(practitioner)
        self.next_id += 1
        return practitioner

    def find_patient(self, search_name):
        # case-insensitive, partial match - see AI Activity Card, Evaluate
        target = search_name.strip().lower()
        return [p for p in self.patients if target in p.name.lower()]

    def book_appointment(self, patient, practitioner, date, time):
        appt = Appointment(self.next_id, patient, practitioner, date, time)
        self.appointments.append(appt)
        self.next_id += 1
        return appt

    def cancel_appointment(self, appointment_id):
        # returns True/False instead of failing silently - see AI Activity Card
        for appt in self.appointments:
            if appt.appointment_id == appointment_id:
                appt.status = "Cancelled"
                return True
        return False

    def history_for(self, patient):
        return [a for a in self.appointments if a.patient is patient]

    def schedule_for(self, practitioner):
        return [a for a in self.appointments
                if a.practitioner is practitioner and a.status != "Cancelled"]

    def status_report(self):
        report = {"Scheduled": 0, "Completed": 0, "Cancelled": 0}
        for a in self.appointments:
            report[a.status] = report.get(a.status, 0) + 1
        return report


def choose_patient(clinic):
    if not clinic.patients:
        print("No patients yet - add one first.")
        return None
    for p in clinic.patients:
        print(f"  {p.patient_id}: {p.name}")
    try:
        chosen_id = int(input("Patient id: "))
    except ValueError:
        print("Not a valid id.")
        return None
    return next((p for p in clinic.patients if p.patient_id == chosen_id), None)


def choose_practitioner(clinic):
    if not clinic.practitioners:
        print("No practitioners yet - add one first.")
        return None
    for pr in clinic.practitioners:
        print(f"  {pr.practitioner_id}: {pr.name} ({pr.specialty})")
    try:
        chosen_id = int(input("Practitioner id: "))
    except ValueError:
        print("Not a valid id.")
        return None
    return next((pr for pr in clinic.practitioners if pr.practitioner_id == chosen_id), None)


def main():
    clinic = Clinic()
    menu = ("\n--- SmartCare v0.1 ---\n"
            "1. Add patient\n2. Add practitioner\n3. Book appointment\n"
            "4. Cancel appointment\n5. Search patient\n6. Patient history\n"
            "7. Practitioner schedule\n8. Status report\n0. Exit")

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            clinic.add_patient(input("Name: "), input("Phone: "))

        elif choice == "2":
            clinic.add_practitioner(input("Name: "), input("Specialty: "))

        elif choice == "3":
            patient = choose_patient(clinic)
            practitioner = choose_practitioner(clinic)
            if patient and practitioner:
                date = input("Date (YYYY-MM-DD): ")
                time = input("Time (HH:MM): ")
                appt = clinic.book_appointment(patient, practitioner, date, time)
                print(f"Booked appointment #{appt.appointment_id}")

        elif choice == "4":
            try:
                appt_id = int(input("Appointment id to cancel: "))
            except ValueError:
                print("Not a valid id.")
                continue
            print("Cancelled." if clinic.cancel_appointment(appt_id)
                  else "No appointment with that id.")

        elif choice == "5":
            results = clinic.find_patient(input("Name to search for: "))
            for p in results:
                print(f"  #{p.patient_id}: {p.name} - {p.phone}")

        elif choice == "6":
            patient = choose_patient(clinic)
            if patient:
                for a in clinic.history_for(patient):
                    print(f"  #{a.appointment_id} with {a.practitioner.name} "
                          f"on {a.date} {a.time} [{a.status}]")

        elif choice == "7":
            practitioner = choose_practitioner(clinic)
            if practitioner:
                for a in clinic.schedule_for(practitioner):
                    print(f"  #{a.appointment_id} {a.patient.name} on {a.date} {a.time}")

        elif choice == "8":
            for status, count in clinic.status_report().items():
                print(f"  {status}: {count}")

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()
