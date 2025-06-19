import streamlit as st
from snowflake.snowpark import Session

# ❗ Hardcoded credentials — replace these with your actual values
connection_parameters = {
    "account": "wlwpzhz-pbb21586",      # Your Snowflake account (e.g., abc-xy12345)
    "user": "CHE1313",
    "password": "Che@1234567890",
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "odoo",
    "schema": "PUBLIC"
}

# Create Snowflake session
session = Session.builder.configs(connection_parameters).create()

# App title
st.title(f"Streamlit + Snowflake (Hardcoded) 🎈 {st.__version__}")

# UI input
hifives_val = st.slider("Number of high-fives in Q3", 0, 90, 60)

# Snowflake Snowpark DataFrame
created_dataframe = session.create_dataframe(
    [[50, 25, "Q1"], [20, 35, "Q2"], [hifives_val, 30, "Q3"]],
    schema=["HIGH_FIVES", "FIST_BUMPS", "QUARTER"]
)

# Convert to Pandas
queried_data = created_dataframe.to_pandas()

# Display bar chart and data table
st.subheader("Number of high-fives")
st.bar_chart(queried_data, x="QUARTER", y="HIGH_FIVES")

st.subheader("Underlying data")
st.dataframe(queried_data, use_container_width=True)
