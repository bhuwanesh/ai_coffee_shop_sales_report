import sqlite3

def best_selling_items(conn):
    cursor = conn.cursor()

    # Total quantity sold per item, highest first
    cursor.execute("""
        SELECT
            m.name,
            SUM(oi.quantity) AS total_sold
        FROM order_items oi
        JOIN menu_items m ON oi.item_id = m.item_id
        GROUP BY m.item_id
        ORDER BY total_sold DESC
    """)

    rows = cursor.fetchall()

    print("\n--- Best-Selling Menu Items ---")
    for rank, (name, total_sold) in enumerate(rows, start=1):
        print(f"{rank}. {name}: {total_sold} sold")

if __name__ == "__main__":
    conn = sqlite3.connect("coffee_shop.db")
    best_selling_items(conn)
    conn.close()
