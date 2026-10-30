"""HeatWatch NYC · evidence review dashboard.

This is NOT the original model or deployment. It presents supplied aggregate
CSV/JSON results and optionally displays an authentic, user-provided risk list.
"""
from pathlib import Path
import pandas as pd
import streamlit as st

BASE = Path(__file__).resolve().parent
st.set_page_config(page_title="HeatWatch NYC · Evidence Review", page_icon="🏙️", layout="wide")
st.title("HeatWatch NYC | SDG 11")
st.caption("Group 11 · Mert Sürmeli · Mehmet Batu Solar · Abdurrahman Dıraz")
st.warning("Evidence-review dashboard only. Original training code, trained model and live 2026–27 scoring pipeline were not supplied; this page does not predict new cases.")

@st.cache_data
def load_csv(relative):
    path = BASE / relative
    return pd.read_csv(path)

summary, validation, inspection = st.tabs(["Overview", "Validation outputs", "Optional authentic ranking"])
with summary:
    st.subheader("Study design")
    st.write("Prediction: for each HPD-registered building, as of September 30, whether at least one heating/hot-water 311 complaint will occur in the following Oct–May winter (H1). Secondary H2 ≥3 complaints.")
    a,b,c = st.columns(3)
    a.metric("Reported building universe", "183,417")
    b.metric("Test ROC-AUC (rolling summary)", "0.8853")
    c.metric("Unresolved label permutation ROC-AUC", "0.4464")
    val = load_csv("results/stage5c/taskB_pluto_val_results.csv")
    view = val.loc[val["model"].str.contains("HistGB", na=False), ["model", "ROC_AUC", "PR_AUC", "Brier"]]
    st.subheader("2024–25 validation: PLUTO and HPD contribution")
    st.dataframe(view, use_container_width=True, hide_index=True)
    chart = view.set_index("model")[["ROC_AUC"]]
    st.bar_chart(chart)
    st.info("The data above are validation scores; they do not estimate the effectiveness of an inspection or energy poverty.")
with validation:
    st.subheader("Rolling winter backtests")
    rolling=load_csv("results/stage6c/s6c_A_rolling.csv")
    st.dataframe(rolling, use_container_width=True, hide_index=True)
    st.line_chart(rolling.set_index("test_kisi")[["egitim_ROC","test_ROC"]])
    st.subheader("Unseen buildings")
    st.dataframe(load_csv("results/stage6c/s6c_C_unseen_buildings.csv"),hide_index=True,use_container_width=True)
    st.subheader("Model complexity")
    st.dataframe(load_csv("results/stage6c/s6c_B_complexity.csv"),hide_index=True,use_container_width=True)
    st.warning("Permutation ROC-AUC 0.4464 remains unexplained. See docs/LIMITATIONS.md.")
with inspection:
    st.subheader("Inspect an authentic precomputed shortlist")
    st.write("Upload a permitted CSV exported by the original HeatWatch pipeline. This app does not generate model probabilities.")
    f=st.file_uploader("Building-risk CSV (optional)",type=["csv"])
    if f is None:
        st.info("No authentic risk CSV supplied. To publish the original predictive demo, add the actual training notebook/model/risk-export pipeline first.")
    else:
        risk=pd.read_csv(f, dtype={"bbl":"string"})
        required={"bbl","risk_probability"}
        if not required.issubset(risk.columns):
            st.error("CSV must contain 'bbl' and 'risk_probability'.")
        else:
            risk["risk_probability"]=pd.to_numeric(risk["risk_probability"], errors="coerce")
            risk=risk[risk["risk_probability"].between(0,1)].copy()
            if "borough" in risk.columns:
                boro=st.multiselect("Borough",sorted(risk["borough"].dropna().astype(str).unique()),default=[])
                if boro:risk=risk[risk["borough"].astype(str).isin(boro)]
            budget=st.slider("Maximum buildings",100,20000,1000,step=100)
            ranked=risk.sort_values("risk_probability",ascending=False).head(budget)
            st.dataframe(ranked,hide_index=True,use_container_width=True)
            st.download_button("Download selected rows",ranked.to_csv(index=False).encode("utf-8"),"heatwatch_selected.csv","text/csv")
            st.caption("Scores are read unchanged from the uploaded file; no new predictions are performed. Do not use for automatic enforcement.")
