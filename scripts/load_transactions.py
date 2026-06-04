import pandas as pd

from app.database import SessionLocal
from app.models import Transaction

db = SessionLocal()

df = pd.read_csv(
    "data/pos/POS-sample-transactions.csv"
)

for _, row in df.iterrows():

    transaction = Transaction(
        order_id=str(row["order_id"]),
        store_id=str(row["store_id"]),
        order_date=str(row["order_date"]),
        order_time=str(row["order_time"]),
        total_amount=float(row["total_amount"])
    )

    db.add(transaction)

db.commit()

print(
    "Transactions Loaded:",
    db.query(Transaction).count()
)

db.close()