import streamlit as st

def show():
    st.title("Mengenal Customer Churn")

    # SECTION 1 - Penjelasan Churn
    st.markdown("---")
    st.markdown("### Apa itu customer churn?")
    st.info("""
- **Customer churn** adalah kondisi dimana seorang pelanggan berhenti menggunakan layanan dari suatu perusahaan, dan beralih menggunakan layanan dari perusahaan lain.
- Churn merupakan tantangan utama yang kerap dihadapi oleh industri telekomunikasi dengan kondisi pasar yang dipenuhi persaingan antar penyedia layanan.
- Churn dapat disebabkan pengalaman pelanggan yang tidak memuaskan, harga yang tidak kompetitif, kualitas produk yang buruk, serta ketidaksesuaian layanan yang ditawarkan terhadap kebutuhan pelanggan.  
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
            line-height: 1.4;
            text-align: justify;
            <p style='text-align: center; margin-top: 0; font-weight: bold;'>Harga Tidak Kompetitif</p>
            <p>Harga yang tidak kompetitif dengan pesaing mendorong pelanggan mencari alternatif lain.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='
            background-color: #e8f2fc;
            padding: 16px;
            border-radius: 6px;
            color: #004280;
            line-height: 1.4;
            text-align: justify;
            <p style='text-align: center; margin-top: 0; font-weight: bold;'>Kualitas Layanan Buruk</p>
            <p>Kualitas layanan yang tidak memuaskan dapat mendorong pelanggan untuk churn.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style='
            background-color: #e8f2fc;
            padding: 16px;
            border-radius: 6px;
            color: #004280;
            line-height: 1.4;
            text-align: justify;
            <p style='text-align: center; margin-top: 0; font-weight: bold;'>Tidak Memenuhi Kebutuhan</p>
            <p>Layanan yang ditawarkan tidak relevan dengan kebutuhan dan preferensi pelanggan.</p>
        </div>
        """, unsafe_allow_html=True)

    
    #with col1:
        #st.info(" **Harga Tidak Kompetitif**\n\nHarga yang tidak kompetitif dengan pesaing mendorong pelanggan mencari alternatif lain.")
    #with col2:
        #st.info(" **Kualitas Layanan Buruk**\n\nKualitas layanan yang tidak memuaskan mendorong pelanggan untuk churn.")
    #with col3:
        #st.info(" **Tidak Memenuhi Kebutuhan**\n\nLayanan yang ditawarkan tidak relevan dengan kebutuhan dan preferensi pelanggan.")

    st.markdown("---")

    # SECTION 2 - Mengapa Deteksi Churn Penting?
    st.markdown("### 🚨 Mengapa Harus Peduli dengan Churn?")
    st.info("""
- Kehilangan pelanggan artinya kehilangan pendapatan tetap.
- Biaya mencari pelanggan baru **5x lebih mahal** daripada mempertahankan pelanggan lama.
- Deteksi churn lebih awal memberi kesempatan melakukan intervensi.
""")

    st.markdown("---")

    # SECTION 4 - Peran Machine Learning
    st.markdown("### 📖 Bagaimana Machine Learning Membantu?")
    st.info("""
Dengan data historis pelanggan, kita dapat:
- Memprediksi siapa saja yang berisiko churn.
- Menggunakan algoritma seperti **XGBoost** yang kuat dalam klasifikasi.
- Mengoptimasi prediksi dengan **SMOTE-ENN** untuk menangani ketidakseimbangan data.
""")
