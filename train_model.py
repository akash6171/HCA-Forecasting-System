import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

df = pd.read_csv("sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year
df["Quarter"] = df["Date"].dt.quarter
df["Week"] = df["Date"].dt.isocalendar().week.astype(int)
df["DayOfWeek"] = df["Date"].dt.dayofweek
df["IsWeekend"] = (df["DayOfWeek"] >= 5).astype(int)

cat_cols = [
    'Store ID',
    'Product ID',
    'Category',
    'Region',
    'Weather Condition',
    'Seasonality'
]

encoders = {}

for col in cat_cols:
    le = LabelEncoder()
    df[col+"_enc"] = le.fit_transform(df[col])
    encoders[col] = le

FEATURES = [
    'Month','Year','Quarter','Week','DayOfWeek','IsWeekend',
    'Price','Discount','Inventory Level',
    'Units Ordered','Competitor Pricing',
    'Promotion','Epidemic',
    'Store ID_enc','Product ID_enc',
    'Category_enc','Region_enc',
    'Weather Condition_enc',
    'Seasonality_enc'
]

X = df[FEATURES]
y = df["Demand"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = RandomForestRegressor(
    n_estimators=100, max_depth=None, min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train,y_train)

joblib.dump(model,"model.pkl", compress=3)
joblib.dump(encoders,"encoders.pkl")

print("Model Saved")