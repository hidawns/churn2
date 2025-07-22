import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io

def show():
    st.title("📊 Dataset: IBM Telco Customer Churn")

    df = pd.read_csv("IBM Churn.csv")
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'}).astype('object')

    # === Statistik Dataset ===
    with st.expander("📊 Statistik Dataset", expanded=True):
        total_rows = df.shape[0]
        total_columns = df.shape[1]
        target_col = 'Churn'
        feature_cols = df.drop(columns=[target_col]).shape[1] if target_col in df.columns else total_columns
        target_count = 1 if target_col in df.columns else 0
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Jumlah Baris**\n\n{total_rows}")
        with col2:
            st.info(f"**Jumlah Kolom**\n\n{total_columns}")
        #with col3:
            #st.markdown(" ")
            #st.info(f"**Fitur Numerik**\n\n{feature_cols}")
        #with col4:
            #st.markdown(" ")
            #st.info(f"**Fitur Kategorikal**\n\n{target_count}")

    # === Sampel Dataset ===
    with st.expander("📄 Sampel Data (Top 5 Baris)"):
        st.dataframe(df.head(), use_container_width=True)

    # === Informasi Struktur Data ===
    with st.expander("🔎 Struktur & Tipe Data"):
        info_df = pd.DataFrame({
            'Kolom': df.columns,
            'Tipe Data': df.dtypes.astype(str),
            'Non-Null Count': df.notnull().sum()
        }).reset_index(drop=True)
        st.dataframe(info_df, use_container_width=True)

    # === Deskripsi Statistik Numerik ===
    with st.expander("📈 Deskripsi Statistik (Numerik)"):
        st.dataframe(df.describe(), use_container_width=True)
