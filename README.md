# Smart Industrial Maintenance System (SIMS)

SIMS is a starter intelligent-maintenance platform that combines sensor data, machine-learning models, document knowledge, speech, and multimodal analysis to support industrial fault diagnosis and maintenance decisions.

## Features

- Sensor-data preprocessing and analysis
- LSTM-based sensor modelling
- Image-defect CNN model interface
- Text transformer and embedding utilities
- PDF knowledge extraction
- Speech-to-text utilities
- Agent modules for perception, diagnosis, knowledge, actions, and audit logging
- Optional OpenAI-powered utilities

## Project structure

```text
SIMS_Project/
├── agents/                 # Perception, diagnosis, knowledge, action, and audit agents
├── config/                 # Pipeline and security configuration
├── data/                   # Sample sensor data and logs
├── documentation/          # Project reports and supporting documents
├── models/                 # ML model components
├── utils/                  # Preprocessing, PDF, speech, and OpenAI helpers
├── main.py                 # Application entry point
├── settings.py             # Environment-backed settings
└── requirements.txt        # Python dependencies
```

## Requirements

- Python 3.10 or newer
- `pip`
- Optional: an OpenAI API key for OpenAI-powered features

## Installation

```bash
git clone https://github.com/kxrtik250/Smart-intelligence-maintenance-system.git
cd Smart-intelligence-maintenance-system
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Set credentials through environment variables rather than placing real secrets in source files.

```powershell
$env:OPENAI_API_KEY = "your-api-key"
$env:JIRA_API_TOKEN = "your-jira-token"
```

The application can run without these optional integrations when the corresponding functionality is not used.

## Run

```bash
python main.py
```

## Development notes

- Generated Python caches, virtual environments, local environment files, and secrets are excluded by `.gitignore`.
- Replace sample data and placeholder configuration with production-approved sources before deployment.
- Review `config/security_config.yaml` and `config/azure_pipeline.yaml` before connecting external services.

## Repository

This project is published at:

https://github.com/kxrtik250/Smart-intelligence-maintenance-system

## License

No license has been selected yet. Add a `LICENSE` file before distributing this project for reuse.
