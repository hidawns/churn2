import streamlit as st
import modules.Home as Home
import modules.Overview as Overview
import modules.Dataset as Dataset
import modules.EDA as EDA
import modules.Inference as Inference

# Sidebar untuk navigasi
st.sidebar.title("📌 Navigasi")
page = st.sidebar.radio("Pilih halaman:", ["🏠 Home", "📖 Overview", "📊 Dataset", "📈 EDA", "🔍 Inference"])

# Simpan state halaman agar bisa diarahkan dari tombol
if 'page' in st.session_state:
    page = st.session_state.page
    del st.session_state.page

# Routing ke halaman sesuai pilihan
if page == "🏠 Home":
    Home.show()
elif page == "📖 Overview":
    Overview.show()
elif page == "📊 Dataset":
    Dataset.show()
elif page == "📈 EDA":
    EDA.show()
elif page == "🔍 Inference":
    Inference.show()
