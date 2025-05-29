import sqlite3

def seed_data():
    conn = sqlite3.connect("car_hire.db")
    cur = conn.cursor()


    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("DROP TABLE IF EXISTS customers")

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


    cur.executemany("INSERT INTO cars (make, model, year) VALUES (?, ?, ?)", [
        ("Toyota", "Corolla", 2020),
        ("Honda", "Civic", 2019),
        ("Ford", "Focus", 2021),
        ("Mazda", "CX-5", 2019)
    ])

    cur.executemany("INSERT INTO customers (name, phone) VALUES (?, ?)", [
        ("Alice Kipyego", "0704578965"),
        ("Bob Kalundu", "0789764646"),
        ("Samuel Eto", "0706784222"),
        ("Jan Peruiyto", "078334666")
    ])

    conn.commit()
    conn.close()
    print("✅ Database seeded successfully.")

if __name__ == "__main__":
    seed_data()
