import streamlit as st
import modules.Home as Home
import modules.Overview as Overview
import modules.Dataset as Dataset
import modules.EDA as EDA
import modules.Inference as Inference

st.set_page_config(layout="wide")  # biar tampilannya dashboard-style

# Sidebar sebagai menu navigasi
with st.sidebar:
    st.markdown("## 📌 Navigasi")
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    if st.button("📖 Overview"):
        st.session_state.page = "Overview"
    if st.button("📊 Dataset"):
        st.session_state.page = "Dataset"
    if st.button("📈 EDA"):
        st.session_state.page = "EDA"
    if st.button("🔍 Inference"):
        st.session_state.page = "Inference"

# Halaman default
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Routing ke halaman sesuai state
if st.session_state.page == "Home":
    Home.show()
elif st.session_state.page == "Overview":
    Overview.show()
elif st.session_state.page == "Dataset":
    Dataset.show()
elif st.session_state.page == "EDA":
    EDA.show()
elif st.session_state.page == "Inference":
    Inference.show()
