import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("📈 Exploratory Data Analysis (EDA)")

    df = pd.read_csv("IBM Churn.csv")
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'}).astype('object')
    df.dropna(inplace=True)

    st.markdown("EDA ini bertujuan untuk memahami karakteristik pelanggan dan faktor-faktor yang berhubungan dengan perilaku churn.")

    # === SECTION: Univariate - Numerical ===
    with st.expander("📊 Univariate Analysis - Variabel Numerik", expanded=True):
        st.markdown("Melihat distribusi numerik: `tenure`, `MonthlyCharges`, `TotalCharges`")

        numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
        fig, axs = plt.subplots(1, 3, figsize=(18, 5))
        for i, col in enumerate(numeric_cols):
            sns.histplot(data=df, x=col, kde=True, ax=axs[i], color="#69b3a2")
            axs[i].set_title(f'Distribusi {col}')
        st.pyplot(fig)

    # === SECTION: Univariate - Categorical ===
    with st.expander("📊 Univariate Analysis - Variabel Kategorik", expanded=False):
        categorical_cols = df.select_dtypes(include='object').drop(columns='customerID').columns
        st.markdown(f"Menampilkan distribusi untuk {len(categorical_cols)} kolom kategorik.")

        fig, axs = plt.subplots(6, 3, figsize=(18, 30))
        axs = axs.ravel()
        for i, col in enumerate(categorical_cols):
            sns.countplot(data=df, x=col, ax=axs[i], color="#3399ff")
            axs[i].set_title(f'{col}', fontweight='bold')
            axs[i].tick_params(axis='x', rotation=45)
        for j in range(len(categorical_cols), len(axs)):
            fig.delaxes(axs[j])
        st.pyplot(fig)

    # === SECTION: Bivariate - Numerik vs Churn ===
    with st.expander("🔎 Bivariate Analysis - Numerik vs Churn", expanded=False):
        st.markdown("Perbandingan numerik berdasarkan churn:")
        
        fig1, axs1 = plt.subplots(1, 3, figsize=(18, 5))
        for i, col in enumerate(numeric_cols):
            sns.boxplot(data=df, x='Churn', y=col, ax=axs1[i], palette='pastel')
            axs1[i].set_title(f'{col} vs Churn')
        st.pyplot(fig1)

        fig2, axs2 = plt.subplots(1, 3, figsize=(18, 6))
        for i, col in enumerate(numeric_cols):
            sns.violinplot(data=df, x='Churn', y=col, ax=axs2[i], palette='Set2')
            axs2[i].set_title(f'{col} vs Churn', fontweight='bold')
        st.pyplot(fig2)

    # === SECTION: Bivariate - Kategorik vs Churn ===
    with st.expander("🔎 Bivariate Analysis - Kategorik vs Churn", expanded=False):
        st.markdown("Distribusi setiap variabel kategorik dibedakan berdasarkan churn.")

        fig, axs = plt.subplots(6, 3, figsize=(18, 30))
        axs = axs.ravel()
        for i, col in enumerate(categorical_cols):
            sns.countplot(data=df, x=col, hue='Churn', ax=axs[i], palette='pastel')
            axs[i].set_title(f'{col} vs Churn', fontweight='bold')
            axs[i].tick_params(axis='x', rotation=45)
        for j in range(len(categorical_cols), len(axs)):
            fig.delaxes(axs[j])
        st.pyplot(fig)

    # === SECTION: Korelasi Heatmap ===
    with st.expander("🌡️ Korelasi antar Variabel Numerik", expanded=False):
        st.markdown("Menganalisis korelasi antar variabel numerik termasuk `Churn` (0/1)")

        df['Churn'] = df['Churn'].map({"No": 0, "Yes": 1})
        numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
        corr = df[numerical_columns].corr()

        plt.figure(figsize=(10, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Heatmap Korelasi Variabel Numerik")
        st.pyplot()
