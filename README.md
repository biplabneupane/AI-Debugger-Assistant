# AI Debugger: Automated Bug Detection & Fixing

## 🚀 Overview
AI Debugger is an automated bug detection and fixing tool that integrates **Flake8 linting, AI-powered debugging (GPT-3.5), execution-based evaluation (Pass@k), and GitHub automation**. The tool scans Python code for errors, categorizes them, suggests AI-generated fixes, and runs unit tests to validate improvements.

## 🎯 Features
- **🔍 Automated Code Analysis**: Uses Flake8 to detect syntax, logic, and stylistic issues.
- **🤖 AI-Powered Fixes**: GPT-3.5 suggests fixes based on categorized errors.
- **🛠 Execution-Based Evaluation**: Uses Pass@k and unit tests to ensure correctness.
- **📦 GitHub Integration**: Automatically commits fixes and opens pull requests.

## 🏗️ Project Structure
```
📦 AI Debugger
├── src
│   ├── analyzer.py        # Parses Flake8 reports and categorizes errors
│   ├── ai_debugger.py     # Uses GPT-3.5 to suggest fixes
│   ├── auto_fixer.py      # Applies fixes and runs tests
│   ├── github_bot.py      # Automates PR creation on GitHub
│   ├── __init__.py        # Package initializer
├── tests
│   ├── test_analyzer.py   # Unit tests for analyzer
│   ├── test_ai_debugger.py # Unit tests for AI debugger
│   ├── test_auto_fixer.py # Unit tests for auto fixer
│   ├── test_github_bot.py # Unit tests for GitHub bot
├── scripts
│   ├── setup_env.sh       # Setup script
│   ├── run_debugger.py    # Runs full debugging pipeline
├── docs
│   ├── research_notes.md  # Documentation & references
│   ├── installation.md    # Setup instructions
│   ├── usage.md           # How to use AI Debugger
├── .github
│   ├── workflows
│   │   ├── lint.yml       # Runs Flake8 on PRs
│   │   ├── debug.yml      # Automates AI debugging pipeline
├── requirements.txt       # Dependencies
├── README.md              # Project Overview
├── LICENSE                # Open-source license
├── CONTRIBUTING.md        # Contribution guidelines
```

## 🛠 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/biplab4/AI-Debugger-Assistant.git
```

### 2️⃣ Create & Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up API Keys
- **GPT-3.5 API Key**: Store it as an environment variable:
  ```sh
  export OPENAI_API_KEY="your-api-key"
  ```
- **GitHub Token (for PR automation)**: Store it in `.env` file:
  ```sh
  GITHUB_TOKEN=your-github-token
  ```

## 🚀 Usage
### Run Full Debugging Pipeline
```sh
python scripts/run_debugger.py
```
### Run Individual Components
```sh
python src/analyzer.py  # Run error detection
python src/ai_debugger.py  # Generate AI fixes
python src/auto_fixer.py  # Apply fixes & run tests
python src/github_bot.py  # Push fixes to GitHub
```

## 🔬 How It Works
1. **Analyze Code:** Detects errors using Flake8 and categorizes them.
2. **AI Fix Generation:** GPT-3.5 generates bug fixes.
3. **Apply Fixes & Test:** Fixes are applied and tested using `pytest`.
4. **Evaluation:** Pass@k and test results are logged.
5. **GitHub Integration:** Fixes are committed and a PR is created.

## 🤝 Contributing
We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact
For issues and feature requests, create an [issue](https://github.com/biplab4/AI-Debugger-Assistant/issues) or contact [biplabneupane43@gmail.com](mailto:biplabneupane43@gmail.com).

 
