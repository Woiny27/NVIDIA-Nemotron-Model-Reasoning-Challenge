# NVIDIA Nemotron Model Reasoning Challenge Workflow

This repository contains an organized, end-to-end pipeline developed in Google Colab for the **NVIDIA Nemotron Model Reasoning Challenge**. The workflow downloads competition datasets, processes reasoning prompts, and uses optimized causal language models (e.g., Phi-2 / DistilGPT2) to generate structured evaluation outputs.

---

## 🚀 Getting Started & Authentication

Because this workspace runs in a cloud environment detached from Kaggle, you must authenticate your API credentials before downloading the competition data.

### 1. Setup Kaggle API Credentials
1. Go to your **Kaggle Account Settings** -> **API** section.
2. Click **Create New API Token** to download your personal `kaggle.json`.
3. Open your Colab file explorer (folder icon on the left sidebar) and upload `kaggle.json` directly to the workspace root.

### 2. Run the Dependency & Dataset Sync
Execute the initialization code block inside the notebook to automatically configure permissions, move your token to `~/.kaggle/`, and stream the data.

You can use either the Kaggle CLI from the shell or the Kaggle Python API. Example working snippets for Google Colab are below.

- Shell / CLI approach (recommended for simple downloads):

```bash
# In a Colab code cell (prefix with ! when running shell commands)
# 1) Install kaggle if it's not already present
!pip install -q kaggle

# 2) Upload kaggle.json via Colab UI, then move it into place and set permissions
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# 3) Download the competition files (replace the competition slug if different)
!kaggle competitions download -c nvidia-nemotron-model-reasoning-challenge -p /content/data

# 4) Unzip downloaded archives (if any)
!unzip -o /content/data/*.zip -d /content/data
```

- Python API approach (using KaggleApi):

```python
# In a Colab python cell
!pip install -q kaggle

from kaggle.api.kaggle_api_extended import KaggleApi
import os

# If you uploaded kaggle.json through the Colab file upload UI, move it into ~/.kaggle
os.makedirs(os.path.expanduser('~/.kaggle'), exist_ok=True)
# If using interactive upload you can use files.upload(); otherwise ensure kaggle.json is present in the workspace
# from google.colab import files
# files.upload()

# Copy the uploaded file into place (this assumes kaggle.json is in the notebook root)
if os.path.exists('kaggle.json'):
    os.replace('kaggle.json', os.path.expanduser('~/.kaggle/kaggle.json'))

os.chmod(os.path.expanduser('~/.kaggle/kaggle.json'), 0o600)

api = KaggleApi()
api.authenticate()

# Download and unzip competition files into ./data
api.competition_download_files('nvidia-nemotron-model-reasoning-challenge', path='data', unzip=True)
print('Data downloaded to:', os.path.abspath('data'))
```

Notes:
- The competition slug used above is `nvidia-nemotron-model-reasoning-challenge`. If the competition uses a different slug, replace it accordingly.
- Ensure `kaggle.json` has correct permissions (600) or the Kaggle client will refuse to use it.

---

Files in this repository
- notebooks/push_from_colab.ipynb — a Colab notebook with secure, ready-to-run cells for pushing commits from Colab (uses in-memory PAT via getpass and http.extraheader).

If you'd like, I can also:
- Add an automated data-check cell that lists the downloaded files and verifies expected files are present.
- Open a PR for the notebook instead of committing directly to main.
