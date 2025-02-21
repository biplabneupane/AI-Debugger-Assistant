import openai
import json

class AIDebugger:
    def __init__(self, api_key, errors_file="errors.json"):
        self.api_key = api_key
        self.errors_file = errors_file

    def get_fix(self, error):
        """Generate a fix using GPT-3.5."""
        prompt = f"""
        The following Python code has a {error['category']}:
        ```
        {error['file']} - Line {error['line']}
        Error: {error['error_message']}
        ```
        Suggest a corrected version of the code.
        """

        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]

    def debug_code(self):
        with open(self.errors_file, "r") as f:
            errors = json.load(f)

        for error in errors:
            fix = self.get_fix(error)
            output_file = f"fixed_{error['file']}"

            with open(output_file, "w") as f:
                f.write(fix)
            print(f"Fixed: {error['file']} -> {output_file}")

if __name__ == "__main__":
    debugger = AIDebugger(api_key="your_openai_api_key")
    debugger.debug_code()

