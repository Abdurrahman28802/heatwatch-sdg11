# Known limitations and open QA checks

1. **Target** is the occurrence of a 311 complaint, not true loss of heat or completed repairs. Reporting propensity differs by area.
2. **Temporal availability:** Contemporary PLUTO v26v2 and HPD registration values are used in earlier periods; this can make backtesting optimistically biased. Check historic vintages.
3. **Label permutation:** Stage 6C supplies ROC-AUC 0.4464, not the approximately 0.50 expected by the stated test design. Original permutation procedure was not shared; repeat within-winter with many seeds and model refits where appropriate.
4. **No independent reconstruction:** Original Colab notebooks and risk list are missing from this review. Test H2 ROC-AUC 0.936 and 10k precision 93.9% are report-stated only.
5. **Population and missingness:** Current HPD registrations cover 73.2% of unique 311-complaint buildings but 95–96% of complaint rows (report values). Do not conflate these denominators. 1–2 unit properties can appear in HPD registrations under specific conditions.
6. **EDA missing groups:** `eda_pluto_by_units.csv` aggregates 182,128 buildings, or 1,289 fewer than 183,417; `eda_pluto_by_age.csv` aggregates 181,134, or 2,283 fewer. Reason is not established from supplied summary CSVs.
7. **Group-rate denominator:** “Listeye giren” rates are selection rates *within each income quartile*, not shares of the total shortlist.
8. **Energy poverty:** Tract median income is not itself a measure of energy burden, indoor thermal conditions, or energy poverty.
9. **Operational decision:** High top-K precision does not prove preventive inspections lower complaints or improve living conditions. Human verification and field trials would be necessary.
10. **Weather:** Correlation −0.864 is descriptive; compare within winter or otherwise account for seasonality.
11. **Original web repository:** Root README at time of update described Assignment 1; do not represent it as the new pipeline until it has been updated.
