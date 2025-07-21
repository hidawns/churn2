import streamlit as st

def show():
    st.title("📊 Churn Prediction Dashboard")
    st.markdown("##### Optimalisasi XGBoost dengan SMOTE-ENN dan GridSearchCV")
    st.write("Dikembangkan oleh: **[Nama Kamu]**")

    st.markdown("---")

    col1, col2 = st.columns([1, 2])
    with col1: 
        st.image("assets/churn_image.jpg", use_container_width=True)
    with col2:
        st.markdown("### 🎯 Tujuan Aplikasi")
        st.info(
            "Aplikasi ini bertujuan untuk memprediksi kemungkinan seorang pelanggan akan **churn** menggunakan model XGBoost "
            "yang telah dioptimasi dengan teknik **SMOTE-ENN** dan **GridSearchCV**."
        )

    st.markdown("---")

    st.markdown("### 🔍 Ingin langsung mencoba prediksi?")
    if st.button("Pergi ke Halaman Prediksi"):
        st.session_state.page = "Inference"
        st.experimental_rerun()
