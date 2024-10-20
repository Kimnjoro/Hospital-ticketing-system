from collections import deque
from ticket_generation import generate_ticket  # Import the ticket generation function

class QueueManager:
    def __init__(self):
        self.queue = deque()

    def add_to_queue(self, ticket_info):
        self.queue.append(ticket_info)

    def call_next_patient(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return "No patients in the queue."

# Simulate the process
if __name__ == "__main__":
    queue_manager = QueueManager()

    # Add patients to queue
    queue_manager.add_to_queue(generate_ticket("John Doe"))
    queue_manager.add_to_queue(generate_ticket("Mary Jane"))

    # Calls the next patient 
    next_patient = queue_manager.call_next_patient()
    print(f"Next patient: {next_patient}")
