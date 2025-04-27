import sqlite3
import pandas as pd

conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT line_items.line_item_id, line_items.quantity, line_items.product_id, 
       products.product_name, products.price
FROM line_items
JOIN products ON line_items.product_id = products.product_id
"""

df = pd.read_sql_query(query, conn)
print(df.head())

df['total'] = df['quantity'] * df['price']
print(df.head())

grouped_df = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
})
print(grouped_df.head())

sorted_df = grouped_df.sort_values('product_name')
print(sorted_df.head())

sorted_df.to_csv('order_summary.csv')

conn.close()
