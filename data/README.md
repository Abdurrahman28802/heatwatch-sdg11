# Data publication policy

Original municipal request-level data, addresses, residential profiles, credentials and 2026–27 building-level rankings are **not** bundled here.

`app.py` can optionally view an **authentic and permitted-for-publication** CSV in the interface. Suggested columns:
- `bbl`: 10-digit building tax-lot key (prefer string, preserve leading zero)
- `risk_probability`: numeric 0..1 calculated by the team’s trained model
- `borough`: optional borough label
- `unitsres`: optional number of dwelling units
- `income_quartile`: optional group G1..G4

The CSV must be actual results from the team, not fabricated demonstration rows. Consider whether publishing an identifiable property ranking poses fairness or privacy risks; a private demo may be preferable.

If a deployed app should read a file by path, use `data/processed/heatwatch_2026_27_risk.csv` locally (ignored in Git). The public repository does not require it to display summary results.
