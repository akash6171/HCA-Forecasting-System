import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="EDA Dashboard",
    layout="wide"
)

st.title("📊 Exploratory Data Analysis Dashboard")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("sales_data.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    df["Revenue"] = (
        df["Price"] * df["Demand"]
    )

    df["Month"] = df["Date"].dt.month
    df["Year"] = df["Date"].dt.year
    df["Quarter"] = df["Date"].dt.quarter

    return df

df = load_data()

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.header("Filters")

category = st.sidebar.multiselect(
    "Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

region = st.sidebar.multiselect(
    "Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

filtered_df = df[
    (df["Category"].isin(category))
    &
    (df["Region"].isin(region))
]

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.subheader("Dataset Overview")

col1,col2,col3,col4,col5 = st.columns(5)

col1.metric(
    "Records",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Products",
    filtered_df["Product ID"].nunique()
)

col3.metric(
    "Stores",
    filtered_df["Store ID"].nunique()
)

col4.metric(
    "Total Demand",
    f"{filtered_df['Demand'].sum():,.0f}"
)

col5.metric(
    "Revenue",
    f"${filtered_df['Revenue'].sum():,.0f}"
)

st.divider()

# ---------------------------------------------------
# MISSING VALUES
# ---------------------------------------------------

st.subheader("Missing Values Analysis")

missing = (
    filtered_df.isnull()
    .sum()
    .reset_index()
)

missing.columns = [
    "Feature",
    "Missing Count"
]

fig = px.bar(
    missing,
    x="Feature",
    y="Missing Count",
    color="Missing Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# DEMAND DISTRIBUTION
# ---------------------------------------------------

st.subheader("Demand Distribution")

col1,col2 = st.columns(2)

with col1:

    fig = px.histogram(
        filtered_df,
        x="Demand",
        nbins=40,
        marginal="box",
        color_discrete_sequence=["#4CAF50"]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig, ax = plt.subplots(
        figsize=(7,4)
    )

    sns.kdeplot(
        filtered_df["Demand"],
        fill=True,
        ax=ax
    )

    st.pyplot(fig)

# ---------------------------------------------------
# MONTHLY TREND
# ---------------------------------------------------

st.subheader("Monthly Demand Trend")

monthly = (
    filtered_df
    .groupby("Month")["Demand"]
    .sum()
    .reset_index()
)

fig = px.line(
    monthly,
    x="Month",
    y="Demand",
    markers=True,
    title="Demand Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# CATEGORY ANALYSIS
# ---------------------------------------------------

st.subheader("Category Analysis")

col1,col2 = st.columns(2)

with col1:

    category_sales = (
        filtered_df
        .groupby("Category")["Demand"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="Demand",
        color="Demand"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.pie(
        category_sales,
        names="Category",
        values="Demand",
        hole=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------------------
# TOP PRODUCTS
# ---------------------------------------------------

st.subheader("Top Products")

top_products = (
    filtered_df
    .groupby("Product ID")["Demand"]
    .sum()
    .sort_values(ascending=False)
    .head(15)
)

fig = px.bar(
    top_products,
    orientation="h"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# REVENUE TREEMAP
# ---------------------------------------------------

st.subheader("Revenue Contribution")

fig = px.treemap(
    filtered_df,
    path=[
        "Category",
        "Product ID"
    ],
    values="Revenue",
    color="Revenue"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# REGION ANALYSIS
# ---------------------------------------------------

st.subheader("Region Analysis")

region_data = (
    filtered_df
    .groupby("Region")["Demand"]
    .sum()
    .reset_index()
)

fig = px.bar(
    region_data,
    x="Region",
    y="Demand",
    color="Demand"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# WEATHER IMPACT
# ---------------------------------------------------

st.subheader("Weather Impact")

fig = px.box(
    filtered_df,
    x="Weather Condition",
    y="Demand",
    color="Weather Condition"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# PROMOTION ANALYSIS
# ---------------------------------------------------

st.subheader("Promotion Impact")

promo = (
    filtered_df
    .groupby("Promotion")["Demand"]
    .mean()
    .reset_index()
)

fig = px.bar(
    promo,
    x="Promotion",
    y="Demand",
    color="Demand"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# INVENTORY VS DEMAND
# ---------------------------------------------------

st.subheader("Inventory vs Demand")

fig = px.scatter(
    filtered_df,
    x="Inventory Level",
    y="Demand",
    color="Category",
    size="Demand"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# CORRELATION HEATMAP
# ---------------------------------------------------

st.subheader("Correlation Analysis")

numeric_df = filtered_df.select_dtypes(
    include=np.number
)

corr = numeric_df.corr()

fig, ax = plt.subplots(
    figsize=(12,8)
)

sns.heatmap(
    corr,
    cmap="coolwarm",
    annot=False,
    ax=ax
)

st.pyplot(fig)

# ---------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------

st.subheader("Business Insights")

highest_month = (
    monthly.loc[
        monthly["Demand"].idxmax(),
        "Month"
    ]
)

highest_region = (
    region_data.loc[
        region_data["Demand"].idxmax(),
        "Region"
    ]
)

best_category = (
    category_sales.loc[
        category_sales["Demand"].idxmax(),
        "Category"
    ]
)

st.success(
    f"""
    📈 Peak Demand Month: {highest_month}

    🏆 Best Performing Region: {highest_region}

    💰 Top Category: {best_category}

    📦 Total Demand: {filtered_df['Demand'].sum():,.0f}
    """
)

# ---------------------------------------------------
# RAW DATA
# ---------------------------------------------------

with st.expander(
    "View Dataset"
):
    st.dataframe(filtered_df)