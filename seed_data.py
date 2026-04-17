import sqlite3

def seed_data(conn):
    cursor = conn.cursor()

    # 8 products across Beverage and Food categories
    menu_items = [
        (1, "Espresso",         "Beverage", 2.50),
        (2, "Latte",            "Beverage", 4.00),
        (3, "Cappuccino",       "Beverage", 3.75),
        (4, "Cold Brew",        "Beverage", 4.50),
        (5, "Croissant",        "Food",     3.00),
        (6, "Blueberry Muffin", "Food",     2.75),
        (7, "Avocado Toast",    "Food",     6.50),
        (8, "Bagel",            "Food",     2.50),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO menu_items VALUES (?, ?, ?, ?)",
        menu_items
    )

    staff = [
        (1, "Sara",  "Barista"),
        (2, "James", "Barista"),
        (3, "Nora",  "Cashier"),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO staff VALUES (?, ?, ?)",
        staff
    )

    # 15 orders spread across different hours and days
    orders = [
        (1,  1, "2024-03-01 08:15:00"),
        (2,  2, "2024-03-01 08:45:00"),
        (3,  3, "2024-03-01 09:10:00"),
        (4,  1, "2024-03-01 09:30:00"),
        (5,  2, "2024-03-01 12:05:00"),
        (6,  3, "2024-03-01 12:20:00"),
        (7,  1, "2024-03-01 13:00:00"),
        (8,  2, "2024-03-02 08:30:00"),
        (9,  3, "2024-03-02 09:00:00"),
        (10, 1, "2024-03-02 09:45:00"),
        (11, 2, "2024-03-02 11:00:00"),
        (12, 3, "2024-03-02 12:30:00"),
        (13, 1, "2024-03-02 13:15:00"),
        (14, 2, "2024-03-03 08:10:00"),
        (15, 3, "2024-03-03 09:20:00"),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO orders VALUES (?, ?, ?)",
        orders
    )

    # 30 line items linking orders to menu items
    order_items = [
        (1,  1,  1, 2), (2,  1,  5, 1),
        (3,  2,  2, 1), (4,  2,  6, 2),
        (5,  3,  3, 1), (6,  3,  7, 1),
        (7,  4,  4, 1), (8,  4,  8, 1),
        (9,  5,  2, 2), (10, 5,  5, 1),
        (11, 6,  1, 1), (12, 6,  6, 1),
        (13, 7,  3, 2), (14, 7,  7, 1),
        (15, 8,  4, 2), (16, 8,  8, 2),
        (17, 9,  2, 1), (18, 9,  5, 2),
        (19, 10, 1, 3), (20, 10, 6, 1),
        (21, 11, 3, 1), (22, 11, 7, 2),
        (23, 12, 4, 1), (24, 12, 5, 1),
        (25, 13, 2, 3), (26, 13, 8, 1),
        (27, 14, 1, 2), (28, 14, 6, 2),
        (29, 15, 3, 1), (30, 15, 7, 1),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO order_items VALUES (?, ?, ?, ?)",
        order_items
    )

    conn.commit()
    print("Sample data inserted.")

if __name__ == "__main__":
    conn = sqlite3.connect("coffee_shop.db")
    seed_data(conn)
    conn.close()
