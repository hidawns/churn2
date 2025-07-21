import streamlit as st
import modules.Home as Home
import modules.Overview as Overview
import modules.Dataset as Dataset
import modules.EDA as EDA
import modules.Inference as Inference

st.set_page_config(page_title="Churn App", layout="wide")

# ==== CSS custom agar tombol sejajar & rapi ====
st.markdown("""
    <style>
    .sidebar-button {
        background-color: #f0f2f6;
        color: black;
        border: 1px solid #ccc;
        border-radius: 0.5rem;
        padding: 0.5rem;
        margin-bottom: 0.5rem;
        text-align: left;
        width: 100%;
        display: block;
        font-weight: 500;
        transition: background-color 0.2s ease;
    }
    .sidebar-button:hover {
        background-color: #e0e0e0;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# ==== Navigasi Sidebar ====
st.sidebar.markdown("## 📌 Navigasi")

# Fungsi buat tombol HTML dengan handler via form
def nav_button(label, target):
    with st.sidebar.form(key=f"nav_{target}"):
        submitted = st.form_submit_button(
            f"{label}",
            help=f"Ke halaman {label}"
        )
        if submitted:
            st.session_state.page = target
        st.markdown(
            f"<button class='sidebar-button'>{label}</button>",
            unsafe_allow_html=True
        )

# Inisialisasi halaman default
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Tombol-tombol navigasi
nav_button("🏠 Home", "Home")
nav_button("📖 Overview", "Overview")
nav_button("📊 Dataset", "Dataset")
nav_button("📈 EDA", "EDA")
nav_button("🔍 Inference", "Inference")

# ==== Routing ke halaman ====
page = st.session_state.page
if page == "Home":
    Home.show()
elif page == "Overview":
    Overview.show()
elif page == "Dataset":
    Dataset.show()
elif page == "EDA":
    EDA.show()
elif page == "Inference":
    Inference.show()
