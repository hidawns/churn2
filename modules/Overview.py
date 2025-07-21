import streamlit as st

def show():
    st.title("Overview")
    st.markdown("### Memahami *Customer Churn* dan Pentingnya Deteksi Dini")

    # SECTION 1 - Penjelasan Konsep
    st.markdown("""**Customer churn** terjadi ketika pelanggan berhenti menggunakan layanan atau produk dari suatu perusahaan.
    Ini adalah indikator penting dalam dunia bisnis, khususnya industri **berbasis langganan** seperti Telekomunikasi, Perbankan, dan SaaS (Software as a Service)
    """)

    st.markdown("---")

    # SECTION 2 - Mengapa Deteksi Churn Penting?
    st.markdown("### 🚨 Mengapa Harus Peduli dengan Churn?")
    st.info("""
- Kehilangan pelanggan artinya kehilangan pendapatan tetap.
- Biaya mencari pelanggan baru **5x lebih mahal** daripada mempertahankan pelanggan lama.
- Deteksi churn lebih awal memberi kesempatan melakukan intervensi.
""")

    st.markdown("---")

    # SECTION 3 - Tindakan Preventif
    st.markdown("### 🎯 Apa yang Bisa Dilakukan Saat Pelanggan Mau Churn?")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(" **Loyalty Program**\n\nTawarkan insentif bagi pelanggan setia.")
    with col2:
        st.info(" **Intervensi Personal**\n\nHubungi pelanggan dengan pendekatan khusus.")
    with col3:
        st.info(" **Diskon Khusus**\n\nBerikan penawaran kompetitif agar pelanggan tetap bertahan.")

    st.markdown("---")

    # SECTION 4 - Peran Machine Learning
    st.markdown("### 📖 Bagaimana Machine Learning Membantu?")
    st.info("""
Dengan data historis pelanggan, kita dapat:
- Memprediksi siapa saja yang berisiko churn.
- Menggunakan algoritma seperti **XGBoost** yang kuat dalam klasifikasi.
- Mengoptimasi prediksi dengan **SMOTE-ENN** untuk menangani ketidakseimbangan data.
""")
