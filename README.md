# Agentic CRM AI

An Agentic AI assistant integrated with your CRM for mortgage/real estate workflows.

### 🚀 Features
- Conversational AI (OpenAI / Anthropic / Local models)
- Orchestration (LangChain / AutoGen / Temporal)
- Actionable APIs: CRM, LOS, Calendar, Email
- Built-in guardrails, compliance, and logging
- AI-assisted code scaffolding via GitHub Actions

### 📦 Quickstart
```bash
# Clone your repo
git clone https://github.com/<your-username>/agentic-crm-ai
cd agentic-crm-ai

# Install dependencies
pip install -r tools/scripts/requirements.txt

# Run the AI scaffolding script
python tools/scripts/generate_scaffold.py --task "scaffold planner + actions"
```

### 🔐 Environment Setup

Copy `.env.example` → `.env` and fill in:

```
OPENAI_API_KEY=sk-...
GITHUB_TOKEN=...
```

### 🧩 CI/CD

- **ai-scaffold.yml**: auto-generates new code via AI prompts
- **ci.yml**: runs linting and tests

### 🧠 Docs

See `/docs/architecture.md` and `/docs/security.md` for detailed architecture, security, and compliance setup.
