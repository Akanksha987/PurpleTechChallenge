# Problem Statement

Detect visitor movement from CCTV footage and generate retail analytics.

# Features

- YOLOv8 Detection
- ByteTrack Tracking
- Entry Detection
- Zone Analytics
- Billing Analytics
- Heatmap
- Funnel
- Conversion Metrics

# Architecture

Video
↓
YOLO
↓
ByteTrack
↓
Events
↓
SQLite
↓
FastAPI
↓
Streamlit

# APIs

GET /stores/{id}/metrics
GET /stores/{id}/heatmap
GET /stores/{id}/funnel
GET /stores/{id}/anomalies

# Run

python -m scripts.create_db
python -m scripts.load_transactions

uvicorn app.main:app --reload

streamlit run dashboard/streamlit_dashboard.py