##TASK 1

import sqlite3

try:
    with  sqlite3.connect("../db/magazines.db") as conn:  # Create the file here, so that it is not pushed to GitHub!
        print("Database created and connected successfully.")
except sqlite3.Error:
    print("Error occurred while creating the database.")
finally:
    conn.close()
    print("Connection closed.")