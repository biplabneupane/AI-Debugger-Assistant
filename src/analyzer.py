import re
import json
import subprocess

class Analyzer:
    ERROR_CATEGORIES = {"E999": "Syntax Error", "F821": "Logic Error", "F401": "Stylistic Issue"}

    def __init__(self, lint_file="lint_report.txt"):
        self.lint_file = lint_file

    def run_flake8(self):
        subprocess.run(["flake8", "--output-file=" + self.lint_file])

    def parse_lint_report(self):
        categorized_errors = []
        with open(self.lint_file, "r") as f:
            for line in f:
                match = re.match(r"(.+):(\d+):(\d+):\s(\w\d+)\s(.+)", line)
                if match:
                    file, line, column, error_code, error_message = match.groups()
                    category = self.ERROR_CATEGORIES.get(error_code, "Other")
                    categorized_errors.append({"file": file, "line": int(line), "error_code": error_code, "category": category})
        with open("errors.json", "w") as json_file:
            json.dump(categorized_errors, json_file, indent=4)

    def analyze(self):
        self.run_flake8()
        self.parse_lint_report()
        print("Analysis completed! Check errors.json")

if __name__ == "__main__":
    Analyzer().analyze()
