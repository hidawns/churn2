import streamlit as st

def show():
    st.title("📖 Overview: Apa itu Customer Churn?")
    st.markdown("""
Customer churn adalah kondisi ketika pelanggan berhenti menggunakan layanan dari suatu perusahaan.  
Hal ini menjadi perhatian serius terutama dalam industri yang berbasis langganan (subscription-based).

**Mengapa deteksi churn penting?**
- 📉 Kehilangan pelanggan = kehilangan pendapatan.
- 💰 Lebih murah mempertahankan pelanggan lama daripada mencari pelanggan baru.
- 🎯 Deteksi dini memungkinkan penawaran/promo agar pelanggan tidak pergi.

**Apa yang bisa dilakukan jika pelanggan berpotensi churn?**
- Penawaran loyalitas
- Layanan personalisasi
- Diskon khusus
- Intervensi langsung dari tim customer success
""")
