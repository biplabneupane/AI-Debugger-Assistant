import os
import anthropic

class AIDebugger:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def get_fix(self, error):
        # Skip API call if running in GitHub Actions
        if os.getenv("GITHUB_ACTIONS"):
            print("⚠️ Running in GitHub Actions – Skipping API Call.")
            return "Mocked fix: This is a placeholder fix since API calls are disabled in CI/CD."

        try:
            response = self.client.messages.create(
                model="claude-2",
                max_tokens=200,
                messages=[{"role": "user", "content": f"Fix this error: {error}"}]
            )
            return response.content
        except anthropic.BadRequestError as e:
            print(f"❌ API Error: {e}")
            return "Error in API call. Check Anthropic credits or usage limits."

    def debug_code(self):
        error = "Example error for testing"
        fix = self.get_fix(error)
        print(f"Suggested fix: {fix}")

if __name__ == "__main__":
    debugger = AIDebugger()
    debugger.debug_code()
