**Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Set up environment variables:**

- Create a `.env` file in the root directory.
- Add your API key:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

**Run the debugger manually (optional):**

```bash
python src/ai_debugger.py
```

