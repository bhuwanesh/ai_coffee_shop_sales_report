import sqlite3

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            item_id     INTEGER PRIMARY KEY,
            name        TEXT NOT NULL,
            category    TEXT NOT NULL,
            price       REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS staff (
            staff_id    INTEGER PRIMARY KEY,
            name        TEXT NOT NULL,
            role        TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id    INTEGER PRIMARY KEY,
            staff_id    INTEGER NOT NULL,
            order_time  TEXT NOT NULL,
            FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id   INTEGER PRIMARY KEY,
            order_id        INTEGER NOT NULL,
            item_id         INTEGER NOT NULL,
            quantity        INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (item_id)  REFERENCES menu_items(item_id)
        )
    """)

    conn.commit()
    print("Database ready. Tables created.")

if __name__ == "__main__":
    conn = sqlite3.connect("coffee_shop.db")
    create_tables(conn)
    conn.close()
