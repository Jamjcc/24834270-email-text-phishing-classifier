# 24834270-email-text-phishing-classifier
CPU-deployable phishing detector from email text — TF-IDF+SVM (cal.) vs BiGRU · Flask demo · F1/PR-AUC/ROC-AUC · notebooks + model artefacts
phishing-email-text-classifier/
├── src/
│   └── serve_app.py          # Flask app (/predict), CPU-only inference
├── models/                   # Tracked with Git LFS
│   ├── tfidf_vectorizer.pkl
│   ├── svm_phishing_model.pkl
│   ├── tokenizer.pkl
│   └── rnn_phishing_model.h5 # BiGRU weights
├── notebooks/
│   └── email_phising.ipynb   # Training & analysis (text pipeline)
├── docs/
│   ├── app.html              # (optional) UI screenshot/static
│   └── figures/              # (optional) PR curves / confusions for README
├── RUN.md                    # Short run & latency notes
├── requirements.txt
├── .gitattributes            # *.pkl / *.h5 via Git LFS
├── .gitignore
├── LICENSE                   # MIT
└── README.md
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
