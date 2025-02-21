# AI Debugger Assistant

AI Debugger Assistant is a tool that helps developers debug their code using AI-powered suggestions. Initially, it used OpenAI's API, but it has now been updated to use Anthropic's Claude API.

## Prerequisites

Before running the AI Debugger Assistant, ensure you have the following installed:

- Python 3.9+
- Required dependencies (install via `pip`)

## Installation

Clone the repository:
```bash
git clone https://github.com/your-repo/AI-Debugger-Assistant.git
cd AI-Debugger-Assistant
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Setting Up API Key

This project now uses Anthropic's Claude API. You need to set up the API key:

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

Alternatively, you can add it to your environment variables in your CI/CD pipeline or local `.env` file.

## Usage

Run the AI Debugger script:
```bash
python src/ai_debugger.py
```

## Configuration

### Using Different Models
You can configure which Claude model to use by modifying `ai_debugger.py`. Currently, the script is set to use:

```python
model="claude-2"
```

You can change it to another available Claude model if needed.

## Troubleshooting

### API Rate Limit Error
If you receive a `429 Rate Limit Error`, ensure that:
- Your API key is correct
- You have sufficient quota in your Anthropic API account

### Module Not Found
If you encounter `ModuleNotFoundError: No module named 'anthropic'`, install the missing package:
```bash
pip install anthropic
```

## Contributing
Pull requests are welcome. Please open an issue for discussion before submitting major changes.

## License
MIT License
