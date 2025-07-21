import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    st.title("📈 Exploratory Data Analysis (EDA)")

    df = pd.read_csv("IBM Churn.csv")
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)

    st.markdown("### 💵 Distribusi Monthly Charges")
    fig1, ax1 = plt.subplots()
    sns.histplot(df['MonthlyCharges'], bins=30, kde=True, ax=ax1)
    st.pyplot(fig1)

    st.markdown("### 📉 Churn vs Tenure")
    fig2, ax2 = plt.subplots()
    sns.boxplot(x='Churn', y='tenure', data=df, ax=ax2)
    st.pyplot(fig2)
