import sqlite3

def seed_data():
    conn = sqlite3.connect("car_hire.db")
    cur = conn.cursor()

    # Drop tables if they exist
    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("DROP TABLE IF EXISTS customers")

    # Create tables
    cur.execute("""
        CREATE TABLE cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT,
            model TEXT,
            year INTEGER,
            is_available INTEGER DEFAULT 1
        )
    """)
    cur.execute("""
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT
        )
    """)

    # Insert sample data
    cur.executemany("INSERT INTO cars (make, model, year) VALUES (?, ?, ?)", [
        ("Toyota", "Corolla", 2020),
        ("Honda", "Civic", 2019),
        ("Ford", "Focus", 2021)
    ])
    cur.executemany("INSERT INTO customers (name, phone) VALUES (?, ?)", [
        ("Alice Johnson", "1234567890"),
        ("Bob Smith", "0987654321")
    ])

    conn.commit()
    conn.close()
    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_data()
