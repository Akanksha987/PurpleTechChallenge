from app.models import Transaction


def get_transaction_count(db):

    return (
        db.query(Transaction)
        .count()
    )