import sqlite3

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(cursor, name, publisher_name):
    cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
    result = cursor.fetchone()
    if result:
        publisher_id = result[0]
        try:
            cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        except sqlite3.IntegrityError:
            print(f"Magazine '{name}' already exists.")
    else:
        print(f"Publisher '{publisher_name}' not found.")

def add_subscriber(cursor, name, address):
    cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
    if cursor.fetchone():
        print(f"Subscriber '{name}' at '{address}' already exists.")
    else:
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))

def add_subscription(cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):
    cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", (subscriber_name, subscriber_address))
    subscriber = cursor.fetchone()
    if not subscriber:
        print(f"Subscriber '{subscriber_name}' at '{subscriber_address}' not found.")
        return

    cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
    magazine = cursor.fetchone()
    if not magazine:
        print(f"Magazine '{magazine_name}' not found.")
        return

    subscriber_id = subscriber[0]
    magazine_id = magazine[0]

    cursor.execute(
        "SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
        (subscriber_id, magazine_id)
    )
    if cursor.fetchone():
        print(f"Subscription already exists for '{subscriber_name}' to '{magazine_name}'.")
        return

    cursor.execute(
        "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
        (subscriber_id, magazine_id, expiration_date)
    )


try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        add_publisher(cursor, "Condé Nast")
        add_publisher(cursor, "Penguin Group")
        add_publisher(cursor, "Hearst Communications")

        add_magazine(cursor, "Vogue", "Condé Nast")
        add_magazine(cursor, "National Geographic", "Penguin Group")
        add_magazine(cursor, "Cosmopolitan", "Hearst Communications")

        add_subscriber(cursor, "Chris", "123 Birch St")
        add_subscriber(cursor, "Kyra", "456 Oak Avenue")
        add_subscriber(cursor, "Tess", "789 Pine Road")

        add_subscription(cursor, "Chris", "123 Birch St", "Vogue", "2025-12-31")
        add_subscription(cursor, "Kyra", "456 Oak Avenue", "National Geographic", "2025-10-01")
        add_subscription(cursor, "Tess", "789 Pine Road", "Cosmopolitan", "2025-11-15")

        conn.commit()
        print("Data inserted successfully.")


except sqlite3.Error as e:
    print(f"An error occurred: {e}")

print("\n--- All Subscribers ---")
cursor.execute("SELECT * FROM subscribers")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\n--- All Magazines (Sorted by Name) ---")
cursor.execute("SELECT * FROM magazines ORDER BY name")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\n--- Magazines Published by 'Condé Nast' ---")
cursor.execute("""
    SELECT magazines.magazine_id, magazines.name, publishers.name 
    FROM magazines 
    JOIN publishers ON magazines.publisher_id = publishers.publisher_id 
    WHERE publishers.name = 'Condé Nast'
""")
rows = cursor.fetchall()
for row in rows:
    print(row)