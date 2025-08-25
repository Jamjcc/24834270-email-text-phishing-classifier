# 24834270-email-text-phishing-classifier
CPU-deployable phishing detector from email text — TF-IDF+SVM (cal.) vs BiGRU · Flask demo · F1/PR-AUC/ROC-AUC · notebooks + model artefacts
# CPU-Deployable Phishing Detection from Email Text
**TF-IDF+SVM (calibrated) vs BiGRU (RNN)** — local, CPU-only demo with a minimal REST UI.

> Primary metric: **F1** (also PR-AUC / ROC-AUC). Inference measured on **CPU** with batch size **1**.

---

## Quickstart

#```bash
# 1) Create & activate a virtualenv
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) Install
pip install -r requirements.txt

# 3) Run the demo (CPU)
python src/serve_app.py
# then open http://127.0.0.1:5000

Data (training) & live feeds (qualitative only)

This project trains only on email text (subject/body). Datasets are not redistributed here; download them directly:

CEAS 2008 Live Spam/Email Corpus — official corpus page
https://plg.uwaterloo.ca/~gvcormac/ceascorpus/

Handle with care; content may be harmful. See site warnings.

Phishing_Legitimate_full.csv (Kaggle) — email-text dataset
https://www.kaggle.com/datasets/amj464/phishing

Live feeds (not used for training — qualitative stress-tests only):

OpenPhish (site & feeds overview) — https://openphish.com/

Community/feeds page — https://openphish.com/phishing_feeds.html

Database product page — https://www.openphish.com/phishing_database.html

PhishTank (site & API) — https://phishtank.org/
 and API info https://phishtank.org/api_info.php

Place any downloaded CSVs under a local data/ folder (ignored by git) if you want to re-run the notebook.
