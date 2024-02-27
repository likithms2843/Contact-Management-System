import sqlite3

# Connect to the database
conn = sqlite3.connect('contacts.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS contacts
             (id INTEGER PRIMARY KEY, name TEXT, cell_number TEXT, email TEXT)''')

# Insert 5 rows of data
contacts_data = [
    ('Alice', '123-456-7890', 'alice@example.com'),
    ('Bob', '234-567-8901', 'bob@example.com'),
    ('Charlie', '345-678-9012', 'charlie@example.com'),
    ('David', '456-789-0123', 'david@example.com'),
    ('Eve', '567-890-1234', 'eve@example.com')
]
c.executemany('INSERT INTO contacts (name, cell_number, email) VALUES (?, ?, ?)', contacts_data)

# Fetch all data and display them on the screen
c.execute('SELECT * FROM contacts')
rows = c.fetchall()
for row in rows:
    print(row)

# Save (commit) the changes
conn.commit()

# C

