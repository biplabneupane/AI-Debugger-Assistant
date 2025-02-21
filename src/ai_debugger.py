import openai
import os
import json

# Load OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

class AIDebugger:
    def __init__(self, errors_file="errors.json"):
        self.errors_file = errors_file
        self.client = openai.OpenAI()  # New OpenAI API client

    def get_fix(self, error):
        """Generate a fix using GPT-3.5-Turbo."""
        prompt = f"""
        The following Python code has a {error['category']}:
        ```
        {error['file']} - Line {error['line']}
        Error: {error['error_message']}
        ```
        Suggest a corrected version of the code.
        """

        response = self.client.chat.completions.create(  # New API method
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI that fixes code errors."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content  # Extract AI-generated fix

    def debug_code(self):
        """Read errors from JSON and generate fixes."""
        with open(self.errors_file, "r") as f:
            errors = json.load(f)

        for error in errors:
            fix = self.get_fix(error)
            output_file = f"fixed_{error['file']}"

            with open(output_file, "w") as f:
                f.write(fix)
            print(f"✅ Fixed: {error['file']} -> {output_file}")

if __name__ == "__main__":
    debugger = AIDebugger()
    debugger.debug_code()
