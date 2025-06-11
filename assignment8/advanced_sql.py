import sqlite3

try:
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()
##TASK 1
    query = """
    SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5
    """

    cursor.execute(query)
    results = cursor.fetchall()
    print("-" * 25)
    print("Task 1\nOrder ID | Total Price")
    print("-" * 25)
    for row in results:
        order_id, total_price = row
        print(f"{order_id:8} | ${total_price:.2f}")
## TASK 2


    query = """
    SELECT c.customer_name, AVG(order_totals.total_price) AS average_total_price
    FROM customers c
    LEFT JOIN (
        SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
    ) order_totals ON c.customer_id = order_totals.customer_id_b
    GROUP BY c.customer_id
    """

    cursor.execute(query)
    results = cursor.fetchall()
    print("-" * 40)
    print("Task 2\nCustomer Name | Average Total Price")
    print("-" * 40)
    for row in results:
        customer_name, average_total_price = row
        if average_total_price is None:
            print(f"{customer_name:30} | N/A")
        else:
            print(f"{customer_name:30} | ${average_total_price:.2f}")



## TASK 3
    conn.execute("PRAGMA foreign_keys = 1")
    conn.execute("BEGIN TRANSACTION")

    try:
        cursor.execute("""
        SELECT customer_id FROM customers 
        WHERE customer_name = 'Perez and Sons'
        """)
        customer_id = cursor.fetchone()[0]

        cursor.execute("""
        SELECT employee_id FROM employees 
        WHERE first_name = 'Miranda' AND last_name = 'Harris'
        """)
        employee_id = cursor.fetchone()[0]

        cursor.execute("""
        SELECT product_id FROM products 
        ORDER BY price ASC 
        LIMIT 5
        """)
        product_ids = [row[0] for row in cursor.fetchall()]

        cursor.execute("""
        INSERT INTO orders (customer_id, employee_id, date) 
        VALUES (?, ?, date('now')) 
        RETURNING order_id
        """, (customer_id, employee_id))

        order_id = cursor.fetchone()[0]

        for product_id in product_ids:
            cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity) 
            VALUES (?, ?, 10)
            """, (order_id, product_id))

        conn.commit()

        cursor.execute("""
        SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = ?
        """, (order_id,))

        results = cursor.fetchall()
        print("-" * 60)
        print("Task 3\nLine Item ID | Quantity | Product Name")
        print("-" * 60)
        for row in results:
            line_item_id, quantity, product_name = row
            print(f"{line_item_id:11} | {quantity:8} | {product_name}")

    except sqlite3.Error as e:
        conn.rollback()
        print(f"Transaction failed: {e}")

## Task 4
    query = """
    SELECT e.first_name, e.last_name, COUNT(o.order_id) AS order_count
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    GROUP BY e.employee_id
    HAVING COUNT(o.order_id) > 5
    ORDER BY order_count DESC
    """

    cursor.execute(query)
    results = cursor.fetchall()
    print("-" * 50)
    print("Task 4\nFirst Name | Last Name | Order Count")
    print("-" * 50)
    for row in results:
        first_name, last_name, order_count = row
        print(f"{first_name:10} | {last_name:9} | {order_count}")

except sqlite3.Error as e:
    print(f"Error occurred: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")
