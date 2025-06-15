
# 🧪 AI-Powered Lab Filter Replenishment Optimization

This project simulates respiratory filter usage for labs using Medicare DME claims data and applies machine learning to identify operational inefficiencies.

## 🎯 Project Goal

To predict and optimize the replacement of respiratory filters (like MicroGard II) in labs based on:
- The number of Pulmonary Function Tests (PFTs)
- The COPD prevalence among patients

## 🧠 What This Project Does

- **Simulates filter demand** using PFT claims and COPD burden
- **Applies Isolation Forest (unsupervised ML)** to detect anomalies in usage
- **Builds a real-time KPI dashboard** using Streamlit
- **Visualizes over- and under-consumption zones**
- **Enables automation insights** for inventory and provider audits

---

## 📊 Tools & Technologies

| Component | Tool |
|----------|------|
| Data Source | Medicare DME CSV (claims + clinical risk) |
| Language | Python |
| Dashboard | Streamlit |
| AI Model | Isolation Forest (sklearn) |
| Visualization | matplotlib, seaborn |
| Forecasting (optional) | Prophet |
| Reporting | Markdown, Jupyter |

---

## 🧩 Key Features

### ✅ Filter Demand Simulation
```python
Filters_Used = DME_Tot_Suplr_Clms × (1 + COPD_Weight) × random_variation
```

### ✅ Anomaly Detection
- Input: `Filters_Used`, `COPD_Weight`
- Model: `IsolationForest(contamination=0.05)`
- Output: `Anomaly` labels for over/under usage

### ✅ Optimization Zones
- 🔴 Over-Consumption
- 🟢 Under-Consumption
- 🔵 Optimal

### ✅ Streamlit Dashboard Includes
- KPI tiles (total, average, flagged)
- Pie chart of optimization zones
- Scatterplot of anomalies
- Provider-level data table

---

## 🔁 AI Automation Ideas

- **Auto-reorder filters** when usage exceeds predicted values
- **Alert system** for over-/under-using labs
- **Weekly anomaly report export**
- **Inventory scaling** based on COPD-driven forecast

---

## 🚀 How to Run This Project

1. Clone the repo:
```bash
git clone https://github.com/yourusername/lab-filter-ai
cd lab-filter-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the dashboard:
```bash
streamlit run dashboards/streamlit_app.py
```

---

## 📁 Folder Structure

```
lab-filter-ai/
├── data/                     # Raw and processed CSVs
├── notebooks/                # Jupyter notebooks for simulation and modeling
├── dashboards/               # Streamlit app
├── reports/                  # Markdown reports and summaries
└── README.md
```

---

## 📸 Example Screenshots

_Add your scatter plot, dashboard UI, and KPI pie chart here._

---

## 🧠 Author

**Ekrem Acar**  
_Applied AI for healthcare operations_  
_Built with Streamlit, sklearn, and real Medicare claims data_

---

## 📜 License

MIT License — use, share, build!
