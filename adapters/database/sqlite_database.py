import sqlite3

conn = sqlite3.connect("testdb1.db")
cursor = conn.cursor()

create_table_transaction_items = """
CREATE TABLE IF NOT EXISTS transactions_items(
transaction_id integer,
product_id integer,
price real,
quantity integer
);
"""

create_table_transactions = """
CREATE TABLE IF NOT EXISTS transactions(
id INTEGER PRIMARY KEY AUTOINCREMENT,
total real,
discount real,
final_total real,
created_at integer
);
"""

cursor.execute(create_table_transactions)
cursor.execute(create_table_transaction_items)

conn.commit()

