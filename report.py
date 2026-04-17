import sqlite3
from best_sellers import best_selling_items
from revenue_by_category import revenue_by_category
from peak_hours import peak_hours
from top_staff import top_staff

def print_divider():
    print("\n" + "=" * 40)

def generate_report(conn):
    print_divider()
    print("       COFFEE SHOP SALES REPORT")
    print_divider()

    best_selling_items(conn)
    print_divider()

    revenue_by_category(conn)
    print_divider()

    peak_hours(conn)
    print_divider()

    top_staff(conn)
    print_divider()

    print("\nReport complete.")

if __name__ == "__main__":
    conn = sqlite3.connect("coffee_shop.db")
    generate_report(conn)
    conn.close()
