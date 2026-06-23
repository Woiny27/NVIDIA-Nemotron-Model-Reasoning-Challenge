import os

# 1. Provide your unique GitHub details
GITHUB_TOKEN = "your_github_personal_access_token_here"
GITHUB_USERNAME = "Woiny27"
REPO_NAME = "NVIDIA-Nemotron-Model-Reasoning-Challenge"

# 2. Configure your Git user profile
!git config --global user.email "your_email@example.com"
!git config --global user.name "Your GitHub Name"

# 3. Initialize the directory, stage the notebook files, and commit locally
!git init
!git add .
!git commit -m "Initial commit: Nvidia Nemotron reasoning challenge workflow"
!git branch -M main

# 4. Inject your token into the remote URL configuration and push
remote_url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
!git remote add origin {remote_url}
!git push -u origin main --force

print("✅ Repository setup complete!")
print("For future commits, use:")
print('  !git add .')
print('  !git commit -m "Your message"')
print('  !git push origin main')
