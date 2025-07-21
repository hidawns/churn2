import streamlit as st

def show():
    st.title("Optimalisasi XGBoost dengan SMOTE-ENN dan GridSearchCV")
    st.markdown("### by [Nama Kamu]")

    image_path = "assets/churn_image.jpg"
    try:
        st.image(image_path, use_container_width=True)
        st.caption("Customer Retention Illustration")
    except FileNotFoundError:
        st.warning("📷 Gambar tidak ditemukan. Pastikan 'assets/churn_image.jpg' ada.")

    st.markdown("#### 🎯 Tujuan Aplikasi")
    st.write("Aplikasi ini bertujuan untuk memprediksi kemungkinan seorang pelanggan akan churn menggunakan model XGBoost yang telah dioptimasi dengan teknik SMOTE-ENN dan GridSearchCV.")

    st.markdown("### 🔍 Langsung ke Prediksi?")
    if st.button("Pergi ke Inference"):
        st.session_state['page'] = '🔍 Inference'
        st.experimental_rerun()
