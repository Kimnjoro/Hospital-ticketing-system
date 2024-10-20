import random

def generate_ticket(patient_name):
    ticket_number = random.randint(100000, 999999)
    ticket_info = {
        "patient_name": patient_name,
        "ticket_number": ticket_number,
        "status": "Valid",
        "department": "General Consultation"
    }
    return ticket_info

# Example ticket generation for a patient
if __name__ == "__main__":
    patient_name = "Kimani Njoroge" # This is an example name which i have put mine
    ticket = generate_ticket(patient_name)
    print(ticket)
