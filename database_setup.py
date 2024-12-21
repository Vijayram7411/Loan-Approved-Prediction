import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('loan_applications.db')
cursor = conn.cursor()

# Create the table to store form submissions
cursor.execute('''
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    income INTEGER NOT NULL,
    credit_score INTEGER NOT NULL,
    pancard_number TEXT NOT NULL,
    existing_loans TEXT,
    pincode TEXT
)
''')

conn.commit()
conn.close()

print("Database setup completed!")
