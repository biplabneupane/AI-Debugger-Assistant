import os
import anthropic  # Use Anthropic Claude API

class AIDebugger:
    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("❌ Error: ANTHROPIC_API_KEY is missing!")

        # ✅ Correct initialization of Anthropic's latest SDK
        self.client = anthropic.Client(api_key=api_key)

    def get_fix(self, error):
        prompt = f"""
        You are an AI that fixes Python errors. Given the following error message, suggest a fix:

        Error: {error}
        """

        response = self.client.messages.create(
            model="claude-3-opus-20240229",  # Use the latest Claude model
            max_tokens=512,
            temperature=0.5,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text  # ✅ Extract response correctly

    def debug_code(self):
        # Simulate a buggy code scenario
        error = "ModuleNotFoundError: No module named 'numpy'"
        fix = self.get_fix(error)
        print("Suggested fix:", fix)

if __name__ == "__main__":
    debugger = AIDebugger()
    debugger.debug_code()
