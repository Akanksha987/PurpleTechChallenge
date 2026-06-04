import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Store Intelligence Dashboard",
    layout="wide"
)

STORE_ID = "ST1008"

st.title("🏪 Purplle Store Intelligence Platform")

metrics = requests.get(
    f"https://purpletechchallenge.onrender.com/stores/{STORE_ID}/metrics"
).json()

heatmap = requests.get(
    f"https://purpletechchallenge.onrender.com/stores/{STORE_ID}/heatmap"
).json()

funnel = requests.get(
    f"https://purpletechchallenge.onrender.com/stores/{STORE_ID}/funnel"
).json()

anomalies = requests.get(
    f"https://purpletechchallenge.onrender.com/stores/{STORE_ID}/anomalies"
).json()

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Visitors",
    metrics.get("unique_visitors", 0)
)

c2.metric(
    "Entries",
    metrics.get("entries", 0)
)

c3.metric(
    "Exits",
    metrics.get("exits", 0)
)

c4.metric(
    "Queue Depth",
    metrics.get("queue_depth", 0)
)

c5.metric(
    "Conversion Rate",
    f"{metrics.get('conversion_rate', 0) * 100:.0f}%"
)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Heatmap Analytics")
    st.json(heatmap)

with right:
    st.subheader("Conversion Funnel")
    st.json(funnel)

st.divider()

st.subheader("Store Anomalies")

if anomalies:
    st.json(anomalies)
else:
    st.success(
        "No anomalies detected"
    )

st.divider()

st.subheader("Store Metrics")

st.dataframe(
    pd.DataFrame(
        [metrics]
    ),
    use_container_width=True
)