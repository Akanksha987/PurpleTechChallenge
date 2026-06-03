from app.database import engine

with engine.connect() as conn:

    result = conn.exec_driver_sql(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table';
        """
    )

    for row in result:
        print(row)