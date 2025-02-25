import os
from dotenv import load_dotenv  # ✅ Load .env file
from github import Github, Auth

# ✅ Load environment variables from .env
load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")

if not github_token:
    raise ValueError("❌ Error: GITHUB_TOKEN is missing! (Check .env file)")

# ✅ Fix deprecated GitHub authentication method
github = Github(auth=Auth.Token(github_token))

# ✅ Print authenticated user
user = github.get_user()
print(f"✅ Authenticated as: {user.login}")
