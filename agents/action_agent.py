import uuid
class ActionAgent:
    def __init__(self):
        pass

    def create_ticket(self, diagnosis_summary, support_docs):
        ticket_id = 'TCKT-' + uuid.uuid4().hex[:8]
        print(f"[ActionAgent] Created ticket {ticket_id} with severity {diagnosis_summary.get('severity')}")
        return ticket_id
