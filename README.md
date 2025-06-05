 Cocacolastic Car Hire Services – Project Overview
This is a command-line application written in Python that simulates a car hire service. Users can interact with the app through a simple menu system to view available cars, hire or return a car, and view customer records.

It uses:

Python classes for modeling data

The built-in sqlite3 module for a local database (no external ORM)

A clean folder structure for scalability

Pre-populated data using a seed script

Test/debug scripts to run during development

Project Structure
bash
Copy
Edit
Cocacolastic-Car-Hire-Services
├── Pipfile              
├── Pipfile.lock          
├── README.md             
└── lib/
    ├── __init__.py
    ├── cli.py            
    ├── debug.py          
    ├── seed.py          
    ├── helpers.py        
    └── models/
        ├── __init__.py
        ├── car.py       
        └── customer.py   
How the Project Works:
1. Seeding the Database (seed.py)
Drops and recreates two tables: cars and customers

Inserts 4 sample car records and 4 sample customers

Saves everything into a local car_hire.db SQLite file


python lib/seed.py
2. Data Models (models/car.py, models/customer.py)
Each model class:

Represents a table in the database

Contains methods for basic CRUD (Create, Read, Update, Delete) operations

Helps keep database logic separated from business logic

Example methods:
Car.get_all_available()
Customer.find_by_id()
Car.mark_unavailable()

3. CLI Interface (cli.py)
This is the main user-facing script. It provides a text menu like:


Welcome to Cocacolastic Car Hire Services!

1. View Available Cars
2. View Customers
3. Hire a Car
4. Return a Car
5. Exit
Based on user input, it:

Fetches and displays data from the database

Calls methods from your Car or Customer classes

Updates the database (e.g., sets is_available = 0 when a car is hired)

4. Development & Debugging (debug.py)
You can test your classes or queries without going through the full CLI flow.


from models.car import Car

cars = Car.get_all()
print(cars)
Run with:


python lib/debug.py
 Relationships in the Data
Right now, my project has a one-to-many structure:

One customer can hire many cars (separately)

Each car can only be hired by one customer at a time (if tracking hires)

In the future, you could:

Add a hires table (many-to-many between cars and customers)

Track when a car was rented and returned

Key Features So Far:
 View all cars or only available ones

 View all customers

 Hire a car (mark it unavailable)

 Return a car (mark it available again)

 Use raw SQL with no external libraries

 Structured code, easy to scale

 Command-line driven — no browser or GUI needed


How to Run the Project:
Install pipenv if not already installed:
pip install pipenv

Install dependencies and activate the virtual environment:
pipenv install
pipenv shell

Seed the database:
python lib/seed.py
Run the main app:
python lib/cli.py
