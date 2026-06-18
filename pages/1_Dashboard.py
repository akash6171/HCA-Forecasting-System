import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

df = pd.read_csv("sales_data.csv")

st.title("📊 Demand Forecasting & Inventory Intelligence Dashboard")

# ======================
# KPI SECTION
# ======================

total_demand = int(df["Demand"].sum())
total_revenue = int((df["Demand"] * df["Price"]).sum())
total_products = df["Product ID"].nunique()
total_stores = df["Store ID"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "📦 Total Demand",
    f"{total_demand:,}"
)

c2.metric(
    "💰 Revenue",
    f"₹ {total_revenue:,.0f}"
)

c3.metric(
    "🏷 Products",
    total_products
)

c4.metric(
    "🏪 Stores",
    total_stores
)

st.markdown("---")

# ======================
# SALES TREND
# ======================

df["Date"] = pd.to_datetime(df["Date"])

monthly = (
    df.groupby(df["Date"].dt.to_period("M"))
    ["Demand"]
    .sum()
    .reset_index()
)

monthly["Date"] = monthly["Date"].astype(str)

fig = px.line(
    monthly,
    x="Date",
    y="Demand",
    title="Monthly Demand Trend",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================
# TOP PRODUCTS + CATEGORY
# ======================

col1, col2 = st.columns(2)

with col1:

    top_products = (
        df.groupby("Product ID")["Demand"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Product ID",
        y="Demand",
        title="🔥 Top 10 Products"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    category_sales = (
        df.groupby("Category")
        ["Demand"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category_sales,
        values="Demand",
        names="Category",
        title="Category Contribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================
# REGION ANALYSIS
# ======================

region_sales = (
    df.groupby("Region")
    ["Demand"]
    .sum()
    .reset_index()
)

fig = px.bar(
    region_sales,
    x="Region",
    y="Demand",
    title="Regional Demand Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================
# WEATHER IMPACT
# ======================

weather = (
    df.groupby("Weather Condition")
    ["Demand"]
    .mean()
    .reset_index()
)

fig = px.bar(
    weather,
    x="Weather Condition",
    y="Demand",
    title="Weather Impact on Demand"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================
# DATA PREVIEW
# ======================

with st.expander("View Dataset"):

    st.dataframe(
        df.head(50),
        use_container_width=True
    )