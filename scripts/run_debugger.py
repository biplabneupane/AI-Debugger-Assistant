import os
from src.ai_debugger import main

if __name__ == "__main__":
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: API key not set. Run `setup_env.sh` first.")
    else:
        main()

