# Data sources and reconstruction notes

The research report claims the following publicly available sources. Values are as reported by the research team; the large raw extracts and collection code were **not** supplied in the handover.

| Data | Identifier | Purpose | Official URL |
|---|---|---|---|
| NYC 311 service requests | `erm2-nwe9` | Heating/hot-water complaint targets and history | https://data.cityofnewyork.us/d/erm2-nwe9 |
| HPD violations | `wvxf-dwi5` | Historic heating/hot-water code violation experiments | https://data.cityofnewyork.us/d/wvxf-dwi5 |
| HPD registrations | `tesw-yqqr` | Current analysis universe of building BBLs | https://data.cityofnewyork.us/d/tesw-yqqr |
| PLUTO | `64uk-42ks` | Building structure and size | https://data.cityofnewyork.us/d/64uk-42ks |
| NOAA daily summaries | `GHCND:USW00094728` Central Park | Descriptive temperature vs complaint analysis | https://www.ncei.noaa.gov/cdo-web/ |
| Census ACS 2024 five-year | `B19013`, `B17001` | Tract-level income/poverty for post-hoc group analysis only | https://api.census.gov/data/2024/acs/acs5 |
| SDG 11 | Target 11.1 | Sustainability framing | https://sdgs.un.org/goals/goal11 |

### Time and leakage constraints
- Target = complaint(s) recorded during a given Oct–May winter.
- Intended prediction point = 30 September immediately before that winter.
- Complaint history should be cut off at the prediction point.
- The **PLUTO v26v2 / HPD registration snapshots are contemporary**, so using them as historic test features may introduce unavailable-at-the-time information. This has not been eliminated with historic snapshots.
- Future winter temperatures must not enter a 30 September model. Observed NOAA data were used only for EDA.
- Current registration population covers **some 1–2-unit buildings** too, not just 3+ unit properties. See https://www.nyc.gov/site/hpd/services-and-information/register-your-property.page

### Aggregates provided
`results/stage5c/` and `results/stage6c/` contain the actual small CSV/JSON results shared for review. They are the only directly reproducible numeric inputs in this package. The rest of the research metrics require the original Colab code and additional output artifacts.
