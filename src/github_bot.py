from dotenv import load_dotenv
import os
from github import Github

# Load .env variables
load_dotenv()

# Get the GitHub token from the .env file
github_token = os.getenv("GITHUB_TOKEN")

if not github_token:
    raise ValueError("❌ Error: GITHUB_TOKEN is missing! Check your .env file.")

# Initialize GitHub API
github = Github(github_token)

# Example: Print authenticated user
user = github.get_user()
print(f"✅ Authenticated as: {user.login}")
