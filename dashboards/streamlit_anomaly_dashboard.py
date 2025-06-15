
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Page config
st.set_page_config(page_title="AI-Powered Filter Anomaly Detection", layout="wide")

# Load the dataset
df = pd.read_csv('../data/mup_dme_ry25_p05_v10_dy22_rfrr.csv', low_memory=False)
df = df.copy()

# Simulate COPD weight and filter usage
df['COPD_Weight'] = df['Bene_CC_PH_COPD_V2_Pct'] / 100
df['Adjusted_Demand'] = df['DME_Tot_Suplr_Clms'] * (1 + df['COPD_Weight'])

np.random.seed(42)
df['Filters_Used'] = df['Adjusted_Demand'] * np.random.uniform(0.9, 1.1, size=len(df))
df['Filters_Used'] = df['Filters_Used'].replace([np.inf, -np.inf], np.nan)
df = df.dropna(subset=['Filters_Used'])
df['Filters_Used'] = df['Filters_Used'].round().astype(int)

# Apply Isolation Forest
features = df[['Filters_Used', 'COPD_Weight']].copy()
model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
df['anomaly_score'] = model.fit_predict(features)
df['Anomaly'] = df['anomaly_score'].map({1: 'Normal', -1: 'Anomaly'})

# Layout
st.title("🔍 AI-Powered Anomaly Detection in Filter Usage")
st.markdown("This section highlights providers with unexpected respiratory filter usage based on COPD prevalence.")

# KPIs
st.subheader("📊 Anomaly Summary")
a1, a2 = st.columns(2)
a1.metric("Total Providers", len(df))
a2.metric("Anomalies Detected", int((df['Anomaly'] == 'Anomaly').sum()))

# Pie chart
st.subheader("⚙️ Anomaly Breakdown")
anomaly_counts = df['Anomaly'].value_counts()
fig1, ax1 = plt.subplots()
anomaly_counts.plot.pie(autopct='%1.1f%%', colors=['red', 'blue'], ax=ax1)
ax1.set_ylabel('')
st.pyplot(fig1)

# Scatter plot
st.subheader("📈 Anomaly Scatter Plot")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=df, x='COPD_Weight', y='Filters_Used', hue='Anomaly', palette={'Anomaly': 'red', 'Normal': 'blue'}, ax=ax2)
plt.xlabel("COPD Prevalence (Weight)")
plt.ylabel("Filters Used")
st.pyplot(fig2)

# Table of anomalies
st.subheader("📋 List of Anomalous Providers")
anomalies = df[df['Anomaly'] == 'Anomaly'][[
    'Rfrg_Prvdr_State_Abrvtn', 'Rfrg_Prvdr_Spclty_Desc',
    'DME_Tot_Suplr_Clms', 'Filters_Used', 'COPD_Weight'
]].sort_values(by='Filters_Used', ascending=False)

st.dataframe(anomalies)
