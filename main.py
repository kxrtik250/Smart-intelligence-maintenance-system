from agents.perception_agent import PerceptionAgent
from agents.diagnosis_agent import DiagnosisAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.action_agent import ActionAgent
from agents.audit_agent import AuditAgent

def main():
    print("🔧 Starting Smart Industrial Maintenance System...")

    perception = PerceptionAgent()
    diagnosis = DiagnosisAgent()
    knowledge = KnowledgeAgent()
    action = ActionAgent()
    audit = AuditAgent()

    multimodal_data = perception.collect_data(
        image_path=None,
        sensor_path="data/sensor_data.csv",
        log_path="data/logs/error_log.txt",
        audio_path=None
    )

    issue_summary = diagnosis.analyze(multimodal_data)
    support_docs = knowledge.search(issue_summary)
    ticket_id = action.create_ticket(issue_summary, support_docs)
    audit.log_activity(issue_summary, ticket_id)

    print(f"Done. Ticket created: {ticket_id}")

if __name__ == '__main__':
    main()
