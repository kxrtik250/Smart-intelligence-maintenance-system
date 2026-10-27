import os
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'replace-with-your-key')
JIRA_API_URL = os.getenv('JIRA_API_URL', 'https://your-jira-instance')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN', 'token')
DB_URL = os.getenv('DB_URL', 'sqlite:///sims.db')
