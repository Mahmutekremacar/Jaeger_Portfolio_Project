
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

## 📁 Folder Structure
Data: https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-referring-provider
```
lab-filter-ai/
├── data/                     # Raw and processed CSVs
├── notebooks/                # Jupyter notebooks for simulation and modeling
├── dashboards/               # Streamlit app
└── README.md
```

---

## 📸 Example Screenshots

![image](https://github.com/user-attachments/assets/d9d01440-ff35-40eb-9e6e-4b17c9a6bb29)
![image](https://github.com/user-attachments/assets/da6b21cb-7865-43ac-9180-848301ce12a4)
![image](https://github.com/user-attachments/assets/a527c9d1-c7d9-45dc-9c19-0f83bdee4ef7)
![image](https://github.com/user-attachments/assets/b9fbbb72-438b-45cb-bb4b-20edb4dd3720)
![image](https://github.com/user-attachments/assets/9ccd59ad-809f-4c07-b9e8-0a827fda7e9e)


---

## 🧠 Author

**Ekrem Acar**  
_Applied AI for healthcare operations_  
_Built with Streamlit, sklearn, and real Medicare claims data_

---

## 📜 License

MIT License — use, share, build!
