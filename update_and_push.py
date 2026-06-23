import os

# 1. Fill in your GitHub details
GITHUB_TOKEN = "your_github_personal_access_token_here"
GITHUB_USERNAME = "your_github_username"
REPO_NAME = "nvidia-nemotron-challenge"  # Your repository name

# 2. Configure your Git profile identity (if not done already)
!git config --global user.email "your_email@example.com"
!git config --global user.name "Your GitHub Name"

# 3. Re-link the remote URL securely using your token
!git remote remove origin
remote_url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
!git remote add origin {remote_url}

# 4. Stage, commit, and push your changes
!git add .
!git commit -m "Updated reasoning workflow"
!git push -u origin main --force

print("✅ Changes pushed successfully!")
