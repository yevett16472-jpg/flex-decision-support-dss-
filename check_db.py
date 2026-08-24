import sqlite3

conn = sqlite3.connect('pasadena_surges.db')
cursor = conn.cursor()

# Get list of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables found:", cursor.fetchall())

conn.close()