import os  # ✅ Fix: Add this at the top

def test_github_token():
    assert os.getenv("GITHUB_TOKEN") is not None  # ✅ Ensures GITHUB_TOKEN exists
