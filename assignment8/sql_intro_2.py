import sqlite3
import pandas as pd

with sqlite3.connect("../db/lesson.db") as conn:

    query = """
    SELECT 
        li.line_item_id,
        li.quantity,
        li.product_id,
        p.product_name,
        p.price
    FROM 
        line_items li
    JOIN 
        products p ON li.product_id = p.product_id
    """
    df = pd.read_sql_query(query, conn)

print("\nRaw Line Item Data")
print(df.head())

df['total'] = df['quantity'] * df['price']
print("\nWith Total Column")
print(df.head())

summary = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
}).reset_index()

summary.rename(columns={
    'line_item_id': 'order_count',
    'total': 'total_sales'
}, inplace=True)

summary.sort_values(by='product_name', inplace=True)

print("\nSummary by Product")
print(summary.head())

summary.to_csv("order_summary.csv", index=False)
print("\n✅ order_summary.csv written successfully.")