import streamlit as st

def show():
    st.title("Mengenal Customer Churn")

    # SECTION 1 - Penjelasan Churn
    #st.markdown("---")
    st.markdown("### Apa itu customer churn?")
    st.markdown("""
- Customer churn adalah kondisi dimana seorang pelanggan berhenti menggunakan layanan dari suatu perusahaan, dan beralih menggunakan layanan dari perusahaan lain.
- Churn merupakan tantangan utama yang kerap dihadapi oleh industri telekomunikasi dengan kondisi pasar yang dipenuhi persaingan antar penyedia layanan.
""")

    # SECTION 2 - Penyebab churn
    st.markdown("---")
    st.markdown("### Penyebab churn pelanggan")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style='
            background-color: #e8f2fc;
            padding: 16px;
            border-radius: 6px;
            color: #004280;
            line-height: 1.5;
        '>
            <div style='text-align: center; font-weight: 650; margin-bottom: 8px;'>Harga Tidak Kompetitif</div>
            <div style='text-align: center;'>Harga yang tidak kompetitif dengan pesaing mendorong pelanggan mencari alternatif lain.</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='
            background-color: #e8f2fc;
            padding: 16px;
            border-radius: 6px;
            color: #004280;
            line-height: 1.5;
        '>
            <div style='text-align: center; font-weight: 650; margin-bottom: 8px;'>Kualitas Layanan Buruk</div>
            <div style='text-align: justify;'>Kualitas layanan yang tidak memuaskan dapat mendorong pelanggan untuk churn.</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style='
            background-color: #e8f2fc;
            padding: 16px;
            border-radius: 6px;
            color: #004280;
            line-height: 1.5;
        '>
            <div style='text-align: center; font-weight: 650; margin-bottom: 8px;'>Tidak Memenuhi Kebutuhan</div>
            <div style='text-align: justify;'>Layanan yang ditawarkan tidak relevan dengan kebutuhan dan preferensi pelanggan.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # SECTION 2 - Dampak Churn
    st.markdown("### Dampak churn pelanggan")
    st.markdown("""
- Tingginya tingkat churn pelanggan dapat menyebabkan penurunan pendapatan perusahaan secara signifikan.
- Perusahaan juga harus mengeluarkan biaya yang lebih besar untuk dapat mengakuisisi pelanggan baru.
- Upaya mengakuisisi pelanggan baru umumnya memakan biaya yang jauh lebih besar, yakni 5-10 kali lipat lebih mahal dibandingkan mempertahankan pelanggan yang sudah ada.
""")

    st.markdown("---")

    # SECTION 4 - Manfaat prediksi churn
    st.markdown("### Manfaat prediksi churn")
    st.info("""
Dengan data historis pelanggan, kita dapat:
- Memprediksi siapa saja yang berisiko churn.
- Menggunakan algoritma seperti **XGBoost** yang kuat dalam klasifikasi.
- Mengoptimasi prediksi dengan **SMOTE-ENN** untuk menangani ketidakseimbangan data.
""")
