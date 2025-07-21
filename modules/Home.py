import streamlit as st

def show():
    st.title("Churn Prediction App")
    st.markdown("##### Optimalisasi Model XGBoost Menggunakan Teknik Hybrid Resampling SMOTE-ENN dan Hyperparameter Tuning GridSearchCV dalam Prediksi Churn Pelanggan")
    st.write("Dikembangkan oleh: Hidayati Tri Winasis")

    st.markdown("---")

    col1, col2 = st.columns([3, 1])
    with col1: 
        st.markdown("\n\n")
        st.markdown("### 🎯 Tujuan Aplikasi")
        st.info(
            "Aplikasi ini bertujuan untuk memprediksi kemungkinan seorang pelanggan akan churn menggunakan model **XGBoost** "
            "yang telah dioptimasi dengan teknik **SMOTE-ENN** dan **GridSearchCV**.")
        st.markdown(" ")
        if st.button("Pergi ke Halaman Prediksi"):
            st.session_state.page = "Inference"
            st.rerun()
    with col2:
        st.image("assets/churn_image.jpg", use_container_width=True)
        
    st.markdown("---")
