import sqlite3

def revenue_by_category(conn):
    cursor = conn.cursor()

    # Total revenue per category: quantity * price, grouped by category
    cursor.execute("""
        SELECT
            m.category,
            ROUND(SUM(oi.quantity * m.price), 2) AS total_revenue
        FROM order_items oi
        JOIN menu_items m ON oi.item_id = m.item_id
        GROUP BY m.category
        ORDER BY total_revenue DESC
    """)

    rows = cursor.fetchall()

    print("\n--- Revenue by Category ---")
    for category, revenue in rows:
        print(f"{category}: ${revenue:.2f}")

if __name__ == "__main__":
    conn = sqlite3.connect("coffee_shop.db")
    revenue_by_category(conn)
    conn.close()
