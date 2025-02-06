import sqlite3

# Connect to the SQLite database (adjust the file name as needed)
conn = sqlite3.connect(f'Match_table_11-12-2024.db')

# Connect to the SQLite database (adjust the file name as needed)
cursor = conn.cursor()

# Query to get all unique championship titles
cursor.execute("SELECT * FROM matches;")

# Fetch and display all championships
championships = cursor.fetchall()
print("Championships in the database:")

# Close the database connection
conn.close()
