import streamlit as st

st.title("Restocking Engine")

inventory = st.number_input(
    "Current Inventory"
)

forecast = st.number_input(
    "Forecast Demand"
)

if st.button("Analyze"):

    safety_stock = forecast * 0.20

    reorder_point = (
        forecast +
        safety_stock
    )

    restock_qty = max(
        0,
        reorder_point - inventory
    )

    if inventory < forecast:
        status = "URGENT RESTOCK"

    elif inventory < reorder_point:
        status = "LOW STOCK"

    else:
        status = "SUFFICIENT STOCK"

    st.metric(
        "Recommended Quantity",
        int(restock_qty)
    )

    st.success(status)