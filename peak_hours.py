import sqlite3

def peak_hours(conn):
    cursor = conn.cursor()

    # Extract the hour from order_time and count orders per hour
    cursor.execute("""
        SELECT
            CAST(strftime('%H', order_time) AS INTEGER) AS hour,
            COUNT(order_id) AS order_count
        FROM orders
        GROUP BY hour
        ORDER BY order_count DESC
    """)

    rows = cursor.fetchall()

    print("\n--- Peak Sales Hours ---")
    for hour, count in rows:
        print(f"{hour:02d}:00 - {hour+1:02d}:00 : {count} orders")

if __name__ == "__main__":
    conn = sqlite3.connect("coffee_shop.db")
    peak_hours(conn)
    conn.close()
