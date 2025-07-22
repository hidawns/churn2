import streamlit as st

def show():
    st.title("Churn Prediction App")
    st.markdown("##### Optimalisasi Model XGBoost Menggunakan Teknik Hybrid Resampling SMOTE-ENN<br>dan Hyperparameter Tuning GridSearchCV dalam Prediksi Churn Pelanggan", unsafe_allow_html=True)
    st.write("Dikembangkan oleh: Hidayati Tri Winasis")

    st.markdown("---")  
    col1, col2 = st.columns([3, 1])
    with col1: 
        st.markdown("""
        <div style='
            background-color: #e8f2fc;
            padding: 16px;
            border-radius: 6px;
            color: #004280;
            line-height: 1.4;
            text-align: justify'>
        Aplikasi ini bertujuan untuk memprediksi kemungkinan seorang pelanggan melakukan churn. Aplikasi dibangun dengan mengimplementasikan machine learning melalui algoritma <b>XGBoost</b> 
        yang dioptimalkan dengan teknik resampling <b>SMOTE-ENN</b> serta hyperparameter tuning <b>GridSearchCV</b>.
        </div>
        """, unsafe_allow_html=True)

        '''
        st.markdown(" ")
        if st.button("**Pergi ke Halaman Prediksi**"):
            st.session_state.page = "Inference"
            st.rerun()
        '''

        st.markdown("""
        <style>
        .blue-button {
            display: inline-block;
            padding: 10px 20px;
            border: 2px solid #1f77b4;
            border-radius: 5px;
            background-color: white;
            color: #1f77b4;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
        }
        .blue-button:hover {
            background-color: #1f77b4;
            color: white;
        }
        </style>
        <a href="#inference" class="blue-button">Pergi ke Halaman Prediksi</a>
    """, unsafe_allow_html=True)

            
    with col2:
        st.image("assets/churn_image.jpg", use_container_width=True)
        
    st.markdown("---")
