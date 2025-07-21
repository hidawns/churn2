import streamlit as st

def show():
    st.title("Churn Prediction App")
    st.markdown("##### Optimalisasi Model XGBoost Menggunakan Teknik Hybrid Resampling SMOTE-ENN dan Hyperparameter Tuning GridSearchCV dalam Prediksi Churn Pelanggan")
    st.write("Dikembangkan oleh: Hidayati Tri Winasis")

    st.markdown("---")

    col1, col2 = st.columns([1, 2])
    with col1: 
        st.image("assets/churn_image.jpg", use_container_width=True)
    with col2:
        st.markdown("###\n\n 🎯 Tujuan Aplikasi")
        st.info(
            "Aplikasi ini bertujuan untuk memprediksi kemungkinan seorang pelanggan akan **churn** menggunakan model XGBoost "
            "yang telah dioptimasi dengan teknik **SMOTE-ENN** dan **GridSearchCV**.")

    st.markdown("---")
    col1, col2 = st.columns([1, 2])
    with col1: 
        st.markdown(" ")
    with col2:
        st.markdown("### 🔍 Ingin langsung mencoba prediksi?")
        if st.button("Pergi ke Halaman Prediksi"):
            st.session_state.page = "Inference"
            st.experimental_rerun()
