# app.py

import streamlit as st
import wandb
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Streamlit Layout ---
st.set_page_config(layout="wide", page_title="House Price Dashboard by Tamaghna Nag")

# --- Branding Header ---
st.markdown("""
    <h1 style='text-align: center; color: teal;'>🏠 House Price Prediction Dashboard</h1>
    <h4 style='text-align: center; color: gray;'>Using OLS, Ridge, Lasso, ElasticNet — powered by 🪄 W&B + Streamlit</h4>
    <hr>
    <div style='text-align: right; color: #999;'>Crafted by <b>Tamaghna Nag</b> | 🇬🇧 London / 🇮🇳 Kolkata</div>
""", unsafe_allow_html=True)

# --- W&B API Setup ---
api = wandb.Api()
run = api.run("nagtamaghna-oxford-vision-and-sensor-technology/house-price-prediction/epl1ivaq")

# --- Metrics Summary ---
st.subheader("📊 Model Metrics Summary")
metrics = run.summary._json_dict

cols = st.columns(4)
model_list = ['OLS', 'Ridge', 'Lasso', 'ElasticNet']

for i, model in enumerate(model_list):
    with cols[i]:
        st.markdown(f"#### 🔍 {model}")
        st.metric("MAE", f"{metrics.get(f'{model}_MAE'):.2f}")
        st.metric("RMSE", f"{metrics.get(f'{model}_RMSE'):.2f}")
        st.metric("R²", f"{metrics.get(f'{model}_R2'):.4f}")

# --- Cross-Validation Comparison Plot ---
st.markdown("---")
st.subheader("📉 Cross-Validation Comparison Plot")
crossval_path = "results/crossvalidationscores.png"

if os.path.exists(crossval_path):
    st.image(crossval_path, caption="📊 Cross-Validated Metrics Comparison", use_container_width=True)
else:
    st.warning("⚠️ Cross-validation plot not found in local directory.")

# --- Lasso Prediction Plot ---
st.markdown("---")
st.subheader("📈 Lasso: Actual vs Predicted Plot")
lasso_plot_path = "results/lassoprediction.png"

if os.path.exists(lasso_plot_path):
    st.image(lasso_plot_path, caption="Predicted vs Actual SalePrice (Lasso)", use_container_width=True)
else:
    st.warning("⚠️ Lasso prediction plot not found. Please generate and save it as `lassoprediction.png`.")

# --- Footer ---
st.markdown("""
    <hr>
    <div style='text-align: center; font-size: 14px; color: gray;'>
        Developed with ❤️ by <b>Tamaghna Nag</b> | ML Engineer | Founder, NovalQ
    </div>
""", unsafe_allow_html=True)
