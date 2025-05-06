import sqlite3

try:
    conn = sqlite3.connect("../db/magazines.db")
    print("Database created.")

    # Enable foreign key constraints
    conn.execute("PRAGMA foreign_keys = 1")

    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS publishers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY,
        magazine_id INTEGER NOT NULL,
        subscriber_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (magazine_id) REFERENCES magazines (id),
        FOREIGN KEY (subscriber_id) REFERENCES subscribers (id)
    )
    ''')

    print("Tables created.")

    ## TASK 3

    def add_publisher(name):
        try:
            cursor.execute("SELECT id FROM publishers WHERE name = ?", (name,))
            if cursor.fetchone():
                return cursor.fetchone()
            else:
                cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
                publisher_id = cursor.lastrowid
                return publisher_id
        except sqlite3.Error as e:
            print(f"Error adding publisher: {e}")
            return None

    def add_magazine(name, publisher_id):
        try:
            cursor.execute("SELECT id FROM magazines WHERE name = ?", (name,))
            if cursor.fetchone():
                return None
            else:
                cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
                magazine_id = cursor.lastrowid
                return magazine_id
        except sqlite3.Error as e:
            print(f"Error adding magazine: {e}")
            return None

    def add_subscriber(name, address):
        try:
            # Check if a subscriber with the same name AND address already exists
            cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", 
                          (name, address))
            if cursor.fetchone():
                return None
            else:
                cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
                subscriber_id = cursor.lastrowid
                return subscriber_id
        except sqlite3.Error as e:
            print(f"Error adding subscriber: {e}")
            return None

    def add_subscription(magazine_id, subscriber_id, expiration_date):
        try:
            if magazine_id is None or subscriber_id is None:
                return None

            cursor.execute("SELECT id FROM subscriptions WHERE magazine_id = ? AND subscriber_id = ?", (magazine_id, subscriber_id))
            if cursor.fetchone():
                return None
            else:
                cursor.execute("INSERT INTO subscriptions (magazine_id, subscriber_id, expiration_date) VALUES (?, ?, ?)", (magazine_id, subscriber_id, expiration_date))
                subscription_id = cursor.lastrowid
                return subscription_id
        except sqlite3.Error as e:
            print(f"Error adding subscription: {e}")
            return None


    # Add publishers
    p1_id = add_publisher("Amazon")
    p2_id = add_publisher("Penguin Random House")
    p3_id = add_publisher("HarperCollins")

    # Add magazines
    m1_id = add_magazine("Time", p1_id)
    m2_id = add_magazine("The New Yorker", p1_id)
    m3_id = add_magazine("National Geographic", p2_id)
    m4_id = add_magazine("Rolling Stone", p3_id)

    # Add subscribers
    s1_id = add_subscriber("John Smith", "123 Main St, New York, NY")
    s2_id = add_subscriber("Bruce Wayne", "Wayne Manor, outside Gotham City")
    s3_id = add_subscriber("Bob Sponge", "124 Conch Street, Bikini Bottom, Pacific Ocean")
    s4_id = add_subscriber("Homer Simpsons", "742 Evergreen Terrace.")

    # Add subscriptions
    add_subscription(m1_id, s1_id, "2026-01-01")
    add_subscription(m2_id, s1_id, "2027-02-03")
    add_subscription(m3_id, s2_id, "2026-04-04")
    add_subscription(m4_id, s3_id, "2027-05-10")
    add_subscription(m1_id, s4_id, "2027-06-11")

    conn.commit()
    print("DB populated.")

    #Task 4

    print("\nQuery 1: All subscribers")
    cursor.execute("SELECT * FROM subscribers")
    for subscriber in cursor.fetchall():
        print(subscriber)

    print("\nQuery 2: All magazines sorted by name")
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    for magazine in cursor.fetchall():
        print(magazine)

    print("\nQuery 3: Magazines published by Amazon")
    cursor.execute("""
        SELECT m.id, m.name, p.name as publisher_name
        FROM magazines m
        JOIN publishers p ON m.publisher_id = p.id
        WHERE p.name = 'Amazon'
    """)
    for magazine in cursor.fetchall():
        print(magazine)


except sqlite3.Error as e:
    print(f"Error occurred: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")
