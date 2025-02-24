import os
from anthropic import Anthropic  # ✅ Correct import

class AIDebugger:
    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("❌ Error: ANTHROPIC_API_KEY is missing!")

        # ✅ Correct Anthropic client initialization
        self.client = Anthropic(api_key=api_key) if hasattr(Anthropic, "api_key") else Anthropic()

    def get_fix(self, error):
        prompt = f"""
        You are an AI that fixes Python errors. Given the following error message, suggest a fix:

        Error: {error}
        """

        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=512,
            temperature=0.5,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["content"]  # ✅ Correct way to extract response

    def debug_code(self):
        error = "ModuleNotFoundError: No module named 'numpy'"
        fix = self.get_fix(error)
        print("Suggested fix:", fix)

if __name__ == "__main__":
    debugger = AIDebugger()
    debugger.debug_code()
