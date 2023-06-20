import sqlite3

def setup_db(db_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Create a new table called 'cars'
    c.execute('''
        CREATE TABLE cars (
            id INTEGER PRIMARY KEY,
            make TEXT,
            model TEXT,
            year INTEGER,
            mileage INTEGER,
            price REAL
        )
    ''')

    # Insert some mock data into the table
    cars = [
        (1, 'Toyota', 'Corolla', 2019, 20000, 15000),
        (2, 'Honda', 'Civic', 2020, 15000, 18000),
        (3, 'Ford', 'Mustang', 2018, 30000, 25000),
        (4, 'Tesla', 'Model 3', 2021, 5000, 40000),
        (5, 'BMW', 'X5', 2020, 25000, 45000),
    ]

    c.executemany("INSERT INTO cars VALUES (?, ?, ?, ?, ?, ?)", cars)

    # Commit the changes and close the connection to the database
    conn.commit()
    conn.close()
