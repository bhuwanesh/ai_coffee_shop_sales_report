import sqlite3

def top_staff(conn):
    cursor = conn.cursor()

    # Total revenue handled per staff member across all four tables
    cursor.execute("""
        SELECT
            s.name,
            s.role,
            ROUND(SUM(oi.quantity * m.price), 2) AS total_sales
        FROM orders o
        JOIN staff s        ON o.staff_id  = s.staff_id
        JOIN order_items oi ON o.order_id  = oi.order_id
        JOIN menu_items m   ON oi.item_id  = m.item_id
        GROUP BY s.staff_id
        ORDER BY total_sales DESC
    """)

    rows = cursor.fetchall()

    print("\n--- Top-Performing Staff ---")
    for rank, (name, role, total_sales) in enumerate(rows, start=1):
        print(f"{rank}. {name} ({role}): ${total_sales:.2f} in sales")

if __name__ == "__main__":
    conn = sqlite3.connect("coffee_shop.db")
    top_staff(conn)
    conn.close()
