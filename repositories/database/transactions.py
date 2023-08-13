import adapters.database.sqlite_database


class TransactionDB:

    def __init__(self, transaction):
        self.transaction = transaction

    def create(self):

        try:
            adapters.database.sqlite_database.cursor.execute(f"""
            INSERT INTO transactions (total, discount, final_total, created_at)
            VALUES (
            {self.transaction.total},
            {self.transaction.discount},
            {self.transaction.final_total}, 
            {self.transaction.created_at}
            )
            """)
            adapters.database.sqlite_database.conn.commit()

            transaction_id = adapters.database.sqlite_database.cursor.lastrowid

            transaction_items_string = []
            for i in self.transaction.items:
                transaction_items_string.append(f"({transaction_id}, {i.product_id}, {i.price}, {i.quantity})")

            values = ",".join(transaction_items_string)

            adapters.database.sqlite_database.cursor.execute(f"""
            INSERT INTO transactions_items (transaction_id, product_id, price, quantity)
            VALUES {values}
            """)

            adapters.database.sqlite_database.conn.commit()
        except Exception as e:
            print(e)
