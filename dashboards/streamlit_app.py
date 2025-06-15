import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Lab Filter Replenishment Dashboard", layout="wide")

# Load data
df = pd.read_csv('../data/mup_dme_ry25_p05_v10_dy22_rfrr.csv', low_memory=False)

# Simulate filter usage
df['COPD_Weight'] = df['Bene_CC_PH_COPD_V2_Pct'] / 100
df['Theoretical_Filters'] = df['DME_Tot_Suplr_Clms']
df['Adjusted_Demand'] = df['Theoretical_Filters'] * (1 + df['COPD_Weight'])

# Simulate a random +/-10% variation in actual usage
np.random.seed(42)
df['Filters_Used'] = df['Adjusted_Demand'] * np.random.uniform(0.9, 1.1, size=len(df))

# Clean non-finite values BEFORE converting to int
df['Filters_Used'] = df['Filters_Used'].replace([np.inf, -np.inf], np.nan)
df = df.dropna(subset=['Filters_Used'])
df['Filters_Used'] = df['Filters_Used'].round().astype(int)

# Recalculate deviation and classify optimization zones
df['Deviation'] = df['Filters_Used'] - df['Adjusted_Demand']

def classify_zone(row):
    if row['Deviation'] > 50:
        return 'Over-Consumption'
    elif row['Deviation'] < -50:
        return 'Under-Consumption'
    else:
        return 'Optimal'

df['Optimization_Zone'] = df.apply(classify_zone, axis=1)

# =======================
# 🎯 Dashboard Layout
# =======================

st.title("🧪 Lab Filter Replenishment Dashboard")
st.markdown("Simulated filter usage based on Medicare DME claims and COPD prevalence. Helps identify over-/under-usage zones.")

# KPIs
st.subheader("📊 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Total Filters Used", int(df['Filters_Used'].sum()))
col2.metric("Avg Filters per Provider", round(df['Filters_Used'].mean(), 1))
col3.metric("Over-Consumers", int((df['Optimization_Zone'] == 'Over-Consumption').sum()))

# Pie chart of optimization zones
st.subheader("⚙️ Optimization Zone Breakdown")
zone_counts = df['Optimization_Zone'].value_counts()
fig1, ax1 = plt.subplots()
zone_counts.plot.pie(autopct='%1.1f%%', colors=['red', 'gold', 'green'], ax=ax1)
ax1.set_ylabel('')
st.pyplot(fig1)

# Scatter plot
st.subheader("📈 Filter Usage vs PFT Claims")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=df, x='DME_Tot_Suplr_Clms', y='Filters_Used', hue='Optimization_Zone', ax=ax2)
plt.xlabel("DME Claims (PFT Tests)")
plt.ylabel("Estimated Filters Used")
st.pyplot(fig2)

# Provider-level data
st.subheader("📋 Provider-Level View")
st.dataframe(df[['Rfrg_Prvdr_State_Abrvtn', 'Rfrg_Prvdr_Spclty_Desc',
                 'DME_Tot_Suplr_Clms', 'Filters_Used', 'Optimization_Zone']].sort_values(by='Filters_Used', ascending=False))
