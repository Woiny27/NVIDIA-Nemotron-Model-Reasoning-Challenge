import os

# 1. Fill in your GitHub details
GITHUB_TOKEN = "your_github_token_here"
GITHUB_USERNAME = "your_github_username"
REPO_NAME = "nvidia-nemotron-challenge" 

# 2. Re-link the remote URL securely using your token
!git remote remove origin
remote_url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
!git remote add origin {remote_url}

# 3. Stage, commit, and push your changes
!git add .
!git commit -m "Updated reasoning workflow"
!git push -u origin main --force

print("✅ Changes pushed successfully to GitHub!")
