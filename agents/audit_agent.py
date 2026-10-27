import json, time
LOGFILE = 'audit_log.jsonl'

class AuditAgent:
    def __init__(self, logfile=LOGFILE):
        self.logfile = logfile

    def log_activity(self, diagnosis_summary, ticket_id):
        entry = {
            'timestamp': time.time(),
            'ticket_id': ticket_id,
            'severity': diagnosis_summary.get('severity'),
            'reasons': diagnosis_summary.get('reasons'),
            'summary': diagnosis_summary.get('short_summary')
        }
        with open(self.logfile,'a',encoding='utf-8') as f:
            f.write(json.dumps(entry) + '\n')
        print(f"[AuditAgent] Logged activity for {ticket_id} -> {self.logfile}")
