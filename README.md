# HeatWatch: NYC heating complaint closure delays

**Samsung Innovation Campus — AI for the SDGs, Assignment 1**  
**Group 11:** Mert Sürmeli, Mehmet Batu Solar, Abdurrahman Dıraz  
**Sustainable Development Goal:** SDG 11 — Sustainable Cities and Communities (Target 11.1)

## What is the project about?

New York City residents can submit 311 service requests when their heat or hot water is not working. We study whether details available **when a request is opened** help predict if the request will remain open for more than **72 hours**. We chose 72 hours as a research threshold, not as an official city service deadline.

An important distinction: **closing a 311 request is not proof that the heating problem was fixed.** Our target is the *administrative closure time*, not repair time.

## Data

- Official source: [NYC Open Data — 311 Service Requests from 2020 to Present](https://data.cityofnewyork.us/d/erm2-nwe9)
- Category: `HEAT/HOT WATER`
- Request creation dates: **October 1, 2024 – May 31, 2025**
- Records retrieved during our analysis: **280,427**
- Records with a usable closing date and nonnegative duration: **276,186**
- Records with missing closing dates excluded from supervised learning: **4,241**

We do not upload the original request-level dataset or names, addresses and precise locations to this repository. The notebook retrieves the public records directly from the official city API. The **summary tables** and **aggregate figures** are included here.

## Exploratory findings

- **17.63%** of usable closed records were closed more than 72 hours after opening.
- Median administrative closure time was **42 hours**.
- The largest number of requests in the selected period occurred in **January 2025**.
- The percentage of records exceeding 72 hours differs by borough. These differences are descriptive and do not establish causation.

Figures created from the study are in [`figures/`](figures/).

## First machine-learning experiment

We use only information known at request opening: **borough, complaint description, month, weekday and hour**. Request closing date or final resolution text is *not* passed into the predictor.

- Training: October 2024 – February 2025 (226,910 records)
- Testing: March 2025 – May 2025 (49,276 records)
- Methods: constant prior baseline, logistic regression, and random forest

| Model | Test ROC-AUC | Test PR-AUC | Test Brier score |
|---|---:|---:|---:|
| Prior-only baseline | 0.500 | 0.052 | 0.0722 |
| Logistic regression | 0.687 | **0.128** | 0.0736 |
| Random forest | **0.697** | 0.124 | **0.0686** |

The results are **preliminary**. The delayed-case percentage is **20.33% during training** but **5.21% during testing**, indicating a strong seasonal shift. At a 0.50 probability threshold, the random forest produced **no positive alerts** on the held-out period. These results do **not** establish a reliable operational warning system.

The exact summary of our original run is in [`results/factual_summary.json`](results/factual_summary.json) and [`results/model_results.csv`](results/model_results.csv). Values may change if the public API records are subsequently updated.

## How to run the notebook

1. Open [Google Colab](https://colab.research.google.com/).
2. Choose **File → Upload notebook** and select [`notebooks/HeatWatch_Assignment1_Colab.ipynb`](notebooks/HeatWatch_Assignment1_Colab.ipynb).
3. Click **Runtime → Run all**. The notebook downloads the selected records from NYC's public API, performs EDA, and compares the first models.
4. The notebook creates charts, model score tables, and a ZIP of local results. **Do not upload the request-level CSV to the public repository.**

For a local Python environment, the required libraries are listed in [`requirements.txt`](requirements.txt). A live internet connection is necessary for downloading the public dataset.

## Repository contents

- [`notebooks/`](notebooks/) — Colab notebook with fetching, EDA, and models
- [`figures/`](figures/) — figures from the original analysis
- [`results/`](results/) — aggregate summary and model scores (no individual requests)
- [`docs/`](docs/) — Assignment 1 concept note and presentation
- [`requirements.txt`](requirements.txt) — Python dependencies

## Limitations and responsible use

- A closed request is not proof of a completed repair.
- Missing closing dates are excluded; this can bias results.
- The data cover reported NYC complaints, not every household with a heating problem.
- Seasonal changes and poor positive-alert recall limit the first models.
- Do not use this prototype to deny, postpone, or deprioritize a resident's service request.
- The 72-hour cutoff is a project definition, not an official SLA or legal requirement.

**Next phase:** improve validation across heating seasons, adjust decision thresholds, and build a small interface that presents uncertainty clearly.
