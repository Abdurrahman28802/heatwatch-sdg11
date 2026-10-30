# HeatWatch NYC · SDG 11

**Building-level prediction of future NYC heating and hot-water 311 complaints**  
Samsung Innovation Campus · Yıldız Technical University · Group 11  
Mert Sürmeli · Mehmet Batu Solar · Abdurrahman Dıraz  
Updated: **30 October 2026**

## What changed since Assignment 1?
Assignment 1 predicted whether a **single complaint would remain open for over 72 hours** in the 2024–25 heating season. The revised research question is:

> On 30 September, can we rank HPD-registered NYC buildings by the chance of receiving at least one heating/hot-water complaint during the following winter (1 Oct–31 May)?

Our secondary H2 target is **at least three complaints during the season**, and a third target is complaint count. These labels capture **reported 311 complaints, not actual defects, repair completion, energy poverty, or causal impact of an inspection**.

## Evidence and reported outcomes

- Six winters: 2020–21 through 2025–26; 1,482,923 311 complaint rows reported in the study.
- Analysis universe: 183,417 building BBLs based on a current HPD registration snapshot.
- NOAA Central Park temperature vs daily complaints: Spearman rho **−0.864** (descriptive, not causal).
- Validation winter 2024–25: 311-history-only HistGB ROC-AUC **0.8452**; +PLUTO **0.8862**; adding HPD violations to 311 history **0.8470**.
- Held-out winter 2025–26: HistGB ROC-AUC **0.8853** from supplied rolling-test summary.
- The 19-page report additionally states **93.9% precision among the top 10,000 buildings** and H2 ROC-AUC **0.936**. These two results are **not independently reconstructible from the supplied Stage 5C/6C summary archives**; original metric outputs and notebook are needed.
- Label-permutation sanity check: ROC-AUC **0.4464**; still unexplained.

**Read [the revised report](docs/HeatWatch_NYC_Rapor_Guncel.pdf) and [presentation](docs/HeatWatch_NYC_Sunum_Guncel.pdf) before interpreting metrics.**

## Repository status / transparency

This package contains:

- Revised report and presentation (`docs/`).
- The *provided* aggregated Stage 5C/6C CSV/JSON outputs (`results/`).
- A small, reproducible **results-review Streamlit dashboard** (`app.py`) that visualizes those aggregate artifacts.
- Local output consistency checks (`scripts/validate_results.py`).
- Data provenance and known limitations (`docs/DATA_SOURCES.md`, `docs/LIMITATIONS.md`).

**Not included in the supplied materials:** original Colab data ingestion/training notebooks, the fitted model artifact, original deployed Streamlit source, raw data, and the per-building 2026–27 risk list. The dashboard is **not** the original live model and **cannot calculate new 2026–27 risk probabilities**. Uploading a genuine per-building risk CSV allows the dashboard to display and export precomputed rankings; it does not train a model.

If you already have Assignment 1 files in this repository, keep them for historical documentation. The original root README should be replaced with this file after preserving a backup; old Assignment 1 analysis does not describe the current target.

## Run the review dashboard

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL displayed by Streamlit. No API tokens or network requests are required to display the supplied summary metrics.

## Run the artifact consistency audit

```bash
python scripts/validate_results.py
```

The audit checks presence, basic schemas and some stated values. It **does not reproduce model training** or validate its fairness/causality claims.

## Additional legacy panel found

A separate user-supplied ZIP (`heatwatch_panel(2).zip`) contained `panel_building_winter.csv` (264,251 rows, 74,299 unique buildings). It **does not match** the current reported 183,417-building evaluation universe and appears to be a historical complaint-history-selected panel. The CSV is deliberately **not included in this public-ready package**. See [legacy panel audit](docs/LEGACY_PANEL_AUDIT.md) for evidence and cautions.

## To complete technical reproducibility

1. Obtain the original Colab `.ipynb` notebooks or `.py` files for NYC 311, HPD, PLUTO, NOAA, ACS ingestion, temporal panel construction, HistGB training, H2, and evaluation.
2. Remove or rotate any API tokens, passwords, personal data, home addresses and request-level records before publication.
3. Include an exact environment/requirements file, fixed seeds and a documented data download procedure.
4. Produce an anonymized/non-identifying per-building risk CSV **only if publication is permitted**, and state whether it is generated from the actual model.
5. Re-run the label-permutation test (within winter, several seeds) and evaluate historical PLUTO/HPD snapshots.
6. Add real Streamlit original source and an operational demo video if submitting as Assignment 2.

## Provenance

See [DATA_SOURCES](docs/DATA_SOURCES.md), [LIMITATIONS](docs/LIMITATIONS.md), and [REVISION_LOG](docs/REVISION_LOG.md). Official data are cited but are not redistributed here.

## Ethical use

Do **not** use this academic ranking to deny municipal services, treat a complaint as proof of a heating failure, infer energy poverty, or automatically prioritize enforcement without human review. Neighborhood reporting biases and current-snapshot limitations remain important.
