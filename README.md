# 📦 Demand Forecasting & Inventory Intelligence System:-

## Overview

The Demand Forecasting & Inventory Intelligence System is a Machine Learning-powered web application designed to predict future product demand and provide intelligent inventory recommendations.

The system analyzes historical sales data along with business factors such as inventory levels, pricing, discounts, promotions, weather conditions, regional information, and seasonality to generate accurate demand forecasts and assist businesses in making inventory management decisions.

The application also includes an interactive Streamlit dashboard that provides business insights, exploratory data analysis, demand forecasting, inventory recommendations, and bulk prediction capabilities.

---

## Key Features:-

### Executive Dashboard
- Business KPI monitoring
- Demand trend visualization
- Category-wise analysis
- Regional performance insights
- Weather impact analysis

### Exploratory Data Analysis (EDA)
- Demand distribution analysis
- Correlation heatmaps
- Seasonal trend analysis
- Promotion impact analysis
- Product performance analysis

### Demand Forecasting
- Single-record demand prediction
- Real-time forecasting interface
- Interactive user inputs

### Inventory Intelligence
- Safety stock calculation
- Reorder point calculation
- Restocking recommendations
- Inventory status monitoring

### Forecast & Restock Planner
- Drag-and-drop CSV upload
- Batch demand prediction
- Batch restocking recommendations
- Download prediction results

### Model Performance Analysis
- Model comparison
- Evaluation metrics
- Forecasting accuracy analysis

---

## Business Problem:-

Businesses often struggle with inventory planning due to inaccurate demand estimation.

Poor forecasting can lead to:

- Stock shortages
- Overstocking
- Increased inventory costs
- Lost sales opportunities
- Inefficient supply chain operations

This project aims to solve these challenges by using Machine Learning techniques to forecast demand and generate inventory recommendations.

---

## Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | Scikit-Learn |
| Model Persistence | Joblib |
| Dashboard | Streamlit |
| Version Control | Git & GitHub |
| Deployment | Streamlit Community Cloud |

---

## Project Structure:

```text
DemandForecastingApp/
│
├── app.py
├── requirements.txt
├── sales_data.csv
├── model.pkl
├── encoders.pkl
│
├── pages/
│   ├── Dashboard.py
│   ├── EDA.py
│   ├── Forecasting.py
│   ├── Restocking.py
│   ├── Model_Performance.py
│   └── Forecast_Restock_Planner.py
│
└── README.md
```

---

## Prerequisites

Before running this project, ensure the following software is installed on your system:

- Python 3.10 or above
- Git
- VS Code (Recommended)
- pip

Verify installation:

```bash
python --version
git --version
pip --version
```

---

## Installation Guide:

### Step 1: Clone Repository:

```bash
git clone https://github.com/akash6171/HCA-Forecasting-System.git
```

Navigate to the project folder:

```bash
cd HCA-Forecasting-System
```

---

### Step 2: Create Virtual Environment

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies:

```bash
pip install -r requirements.txt
```

---

### Step 4: Run Application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

**NOTE:** Ensure the project structure is as same as mentioned above.

---

## Dataset Information:

The dataset contains historical information related to:

- Sales Transactions
- Product Information
- Inventory Levels
- Pricing Details
- Discounts
- Competitor Pricing
- Promotions
- Weather Conditions
- Seasonality
- Regional Information

### Target Variable

```text
Demand
```

---

## Data Preprocessing:

The following preprocessing steps were performed:

- Missing value handling
- Duplicate removal
- Feature engineering
- Date feature extraction
- Label encoding
- Data transformation

### Engineered Features:

- Month
- Year
- Quarter
- Week Number
- Day Of Week
- Weekend Indicator

---

## Machine Learning Models:

The following models were developed and evaluated:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### Evaluation Metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The best-performing model was selected and deployed within the application.

---

## Inventory Intelligence Logic:

The inventory recommendation engine calculates:

### Safety Stock:

```text
Safety Stock = 20% of Forecasted Demand
```

### Reorder Point:

```text
Reorder Point = Forecasted Demand + Safety Stock
```

### Restock Quantity:

```text
Restock Quantity = Reorder Point - Current Inventory
```

### Inventory Status:

- 🟢 Sufficient Stock
- 🟡 Low Stock
- 🔴 Urgent Restock

---

## Batch Prediction:

Users can:

1. Upload CSV files.
2. Generate demand forecasts for multiple records.
3. Calculate safety stock and reorder points.
4. Receive restocking recommendations.
5. Download prediction results.

---

## Deployment:

### GitHub Repository:

Replace with your repository link:

```text
https://github.com/akash6171/HCA-Forecasting-System
```

### Streamlit Deployment:

Replace with your deployment link:

```text
https://hca-forecasting-system-hvms5bkjhnazw6yzi39ei6.streamlit.app
```

---

## Future Enhancements:

- Real-time forecasting
- Deep Learning models
- Automated purchase recommendations
- ERP integration
- Cloud database integration
- API-based forecasting services
- Advanced inventory optimization

---

## Author:

**Akash Kumar**
