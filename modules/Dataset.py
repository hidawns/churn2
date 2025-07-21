import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("📊 Dataset Overview")
    
    df = pd.read_csv("IBM Churn.csv")

    st.markdown("### 📝 Nama Dataset")
    st.write("IBM Telco Customer Churn Dataset")

    st.markdown("### 🧾 Deskripsi Kolom")
    st.write(df.dtypes)

    st.markdown("### 🎯 Kelas Target: `Churn`")
    st.write("Distribusi Kelas:")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Churn', ax=ax)
    st.pyplot(fig)
