import streamlit as st
import modules.Home as Home
import modules.Overview as Overview
import modules.Dataset as Dataset
import modules.EDA as EDA
import modules.Inference as Inference

st.set_page_config(page_title="Churn Prediction App", layout="wide", page_icon="📊")

# === Sidebar Navigasi ===
with st.sidebar:
    st.image("assets/churn_image.jpg", use_column_width=True)
    st.markdown("### 📌 Navigasi")
    
    nav_options = {
        "🏠 Home": "Home",
        "📖 Overview": "Overview",
        "📊 Dataset": "Dataset",
        "📈 EDA": "EDA",
        "🔍 Prediksi": "Inference"
    }

    # Navigasi dengan radio
    selected = st.radio("Pilih Halaman", list(nav_options.keys()))

    # Simpan state
    st.session_state.page = nav_options[selected]

    st.markdown("---")
    st.caption("© 2025 | Churn Prediction App")

# === Routing Halaman ===
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
