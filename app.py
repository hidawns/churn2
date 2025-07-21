import streamlit as st
import modules.Home as Home
import modules.Overview as Overview
import modules.Dataset as Dataset
import modules.EDA as EDA
import modules.Inference as Inference

st.set_page_config(page_title="Churn App", layout="wide")

# === Sidebar Navigasi Custom ===
st.sidebar.markdown("## 📌 Navigasi")

# Atur halaman yang aktif di session_state
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Tombol navigasi
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"
if st.sidebar.button("📖 Overview"):
    st.session_state.page = "Overview"
if st.sidebar.button("📊 Dataset"):
    st.session_state.page = "Dataset"
if st.sidebar.button("📈 EDA"):
    st.session_state.page = "EDA"
if st.sidebar.button("🔍 Inference"):
    st.session_state.page = "Inference"
