import streamlit as st

st.set_page_config(
    page_title="Customer Churn Classifier",
    page_icon="🔍",
    layout="wide"
)

st.sidebar.title("📂 Navigation")
st.sidebar.markdown("Pilih halaman:")
menu = st.sidebar.radio("", ["🏠 Home", "📖 Overview", "📊 Dataset", "📈 EDA", "🔍 Inference"])

if menu == "🏠 Home":
    from pages import Home
    Home.show()
elif menu == "📖 Overview":
    from pages import Overview
    Overview.show()
elif menu == "📊 Dataset":
    from pages import Dataset
    Dataset.show()
elif menu == "📈 EDA":
    from pages import EDA
    EDA.show()
elif menu == "🔍 Inference":
    from pages import Inference
    Inference.show()
