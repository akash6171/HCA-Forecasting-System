import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Batch Prediction", layout="wide")

st.title("📂 Batch Demand Prediction")
st.markdown(
    """
    Upload a CSV or Excel file containing multiple records and get:
    - Demand Forecast
    - Safety Stock
    - Reorder Point
    - Restock Quantity
    """
)

# ==========================
# LOAD MODEL & ENCODERS
# ==========================

model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

# ==========================
# FILE UPLOAD
# ==========================

uploaded_file = st.file_uploader(
    "📂 Upload CSV or Excel File",
    type=["csv", "xlsx", "xls"]
)

if uploaded_file is not None:

    try:

        # ==========================
        # READ FILE
        # ==========================

        file_name = uploaded_file.name.lower()

        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif file_name.endswith((".xlsx", ".xls")):
            df = pd.read_excel(uploaded_file)

        else:
            st.error("Unsupported File Format")
            st.stop()

        st.success("✅ File Uploaded Successfully")

        st.subheader("Uploaded Data Preview")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        # ==========================
        # FEATURE ENGINEERING
        # ==========================

        df["Date"] = pd.to_datetime(df["Date"])

        df["Month"] = df["Date"].dt.month
        df["Year"] = df["Date"].dt.year
        df["Quarter"] = df["Date"].dt.quarter
        df["Week"] = (
            df["Date"]
            .dt
            .isocalendar()
            .week
            .astype(int)
        )

        df["DayOfWeek"] = (
            df["Date"]
            .dt
            .dayofweek
        )

        df["IsWeekend"] = (
            df["DayOfWeek"] >= 5
        ).astype(int)

        # ==========================
        # ENCODING
        # ==========================

        df["Store ID_enc"] = (
            encoders["Store ID"]
            .transform(df["Store ID"])
        )

        df["Product ID_enc"] = (
            encoders["Product ID"]
            .transform(df["Product ID"])
        )

        df["Category_enc"] = (
            encoders["Category"]
            .transform(df["Category"])
        )

        df["Region_enc"] = (
            encoders["Region"]
            .transform(df["Region"])
        )

        df["Weather Condition_enc"] = (
            encoders["Weather Condition"]
            .transform(df["Weather Condition"])
        )

        df["Seasonality_enc"] = (
            encoders["Seasonality"]
            .transform(df["Seasonality"])
        )

        # ==========================
        # MODEL FEATURES
        # ==========================

        FEATURES = [
            'Month',
            'Year',
            'Quarter',
            'Week',
            'DayOfWeek',
            'IsWeekend',
            'Price',
            'Discount',
            'Inventory Level',
            'Units Ordered',
            'Competitor Pricing',
            'Promotion',
            'Epidemic',
            'Store ID_enc',
            'Product ID_enc',
            'Category_enc',
            'Region_enc',
            'Weather Condition_enc',
            'Seasonality_enc'
        ]

        # ==========================
        # PREDICTION BUTTON
        # ==========================

        if st.button("🚀 Predict Demand"):

            predictions = model.predict(
                df[FEATURES]
            )

            df["Predicted_Demand"] = (
                predictions.round(0)
            )

            # ==========================
            # RESTOCKING ENGINE
            # ==========================

            df["Safety_Stock"] = (
                df["Predicted_Demand"] * 0.20
            ).round(0)

            df["Reorder_Point"] = (
                df["Predicted_Demand"] +
                df["Safety_Stock"]
            ).round(0)

            df["Restock_Qty"] = (
                df["Reorder_Point"] -
                df["Inventory Level"]
            ).clip(lower=0).round(0)

            def stock_status(row):

                if row["Inventory Level"] < row["Predicted_Demand"]:
                    return "URGENT RESTOCK"

                elif row["Inventory Level"] < row["Reorder_Point"]:
                    return "LOW STOCK"

                else:
                    return "SUFFICIENT STOCK"

            df["Stock_Status"] = (
                df.apply(
                    stock_status,
                    axis=1
                )
            )

            # ==========================
            # DISPLAY RESULTS
            # ==========================

            st.success(
                "✅ Prediction Completed Successfully"
            )

            st.subheader(
                "Prediction Results"
            )

            st.dataframe(
                df,
                use_container_width=True
            )

            # ==========================
            # SUMMARY METRICS
            # ==========================

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Total Forecast Demand",
                int(df["Predicted_Demand"].sum())
            )

            col2.metric(
                "Products Need Restocking",
                len(
                    df[
                        df["Stock_Status"]
                        != "SUFFICIENT STOCK"
                    ]
                )
            )

            col3.metric(
                "Total Recommended Restock Qty",
                int(df["Restock_Qty"].sum())
            )

            # ==========================
            # DOWNLOAD RESULTS
            # ==========================

            csv = (
                df
                .to_csv(index=False)
                .encode("utf-8")
            )

            st.download_button(
                label="📥 Download Prediction Results",
                data=csv,
                file_name="batch_predictions.csv",
                mime="text/csv"
            )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )

else:

    st.info(
        """
        Supported Formats:
        
        CSV (.csv),
        Excel (.xlsx) or
        Excel (.xls)
        

        Required Columns:
        
        Date,
        Store ID,
        Product ID,
        Category,
        Region,
        Weather Condition,
        Seasonality,
        Price,
        Discount,
        Inventory Level,
        Units Ordered,
        Competitor Pricing,
        Promotion,
        Epidemic
        """
    )