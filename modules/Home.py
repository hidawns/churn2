import streamlit as st

def show():
    st.title("Churn Prediction App")
    st.markdown("##### Optimalisasi Model XGBoost Menggunakan Teknik Hybrid Resampling SMOTE-ENN dan Hyperparameter Tuning GridSearchCV dalam Prediksi Churn Pelanggan")
    st.write("Dikembangkan oleh: Hidayati Tri Winasis")

    st.markdown("---")

    col1, col2 = st.columns([3, 1])
    with col1: 
        st.markdown("### 📌 Tujuan Aplikasi")
        st.info(
            "Aplikasi ini bertujuan untuk memprediksi kemungkinan seorang pelanggan melakukan churn. Aplikasi dibangun dengan mengimplementasikan machine learning melalui algoritma **XGBoost** "
            "yang dioptimalkan dengan **SMOTE-ENN** serta **GridSearchCV**.")
        st.markdown(" ")

        st.markdown("""
            <style>
            div.stButton > button:first-child {
             
                color: white;
                padding: 0.6em 1.2em;
                border-radius: 8px;
                font-weight: bold;
                transition: 0.3s;
            }
            div.stButton > button:first-child:hover {
                background-color: #2878cc;
                color: white;
            }
            </style>
        """, unsafe_allow_html=True)


        
        if st.button("Pergi ke Halaman Prediksi"):
            st.session_state.page = "Inference"
            st.rerun()
    with col2:
        st.image("assets/churn_image.jpg", use_container_width=True)
        
    st.markdown("---")
