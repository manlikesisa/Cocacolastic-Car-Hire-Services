import sqlite3

def connect():
    return sqlite3.connect("car_hire.db")

def list_cars():
    conn = connect()
    cur = conn.cursor()
    for row in cur.execute("SELECT * FROM cars"):
        print(row)
    conn.close()

def list_customers():
    conn = connect()
    cur = conn.cursor()
    for row in cur.execute("SELECT * FROM customers"):
        print(row)
    conn.close()

def hire_car():
    list_cars()
    car_id = input("Enter Car ID to hire: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT is_available FROM cars WHERE id = ?", (car_id,))
    result = cur.fetchone()
    if result and result[0] == 1:
        cur.execute("UPDATE cars SET is_available = 0 WHERE id = ?", (car_id,))
        conn.commit()
        print("Car hired successfully.")
    else:
        print("Car is not available or does not exist.")
    conn.close()

def return_car():
    list_cars()
    car_id = input("Enter Car ID to return: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT is_available FROM cars WHERE id = ?", (car_id,))
    result = cur.fetchone()
    if result and result[0] == 0:
        cur.execute("UPDATE cars SET is_available = 1 WHERE id = ?", (car_id,))
        conn.commit()
        print("Car returned successfully.")
    else:
        print("Car is already available or does not exist.")
    conn.close()

def main():
    while True:
        print("\nCar Hire Service")
        print("1. View Cars")
        print("2. View Customers")
        print("3. Hire Car")
        print("4. Return Car")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            list_cars()
        elif choice == "2":
            list_customers()
        elif choice == "3":
            hire_car()
        elif choice == "4":
            return_car()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
