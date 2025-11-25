# Write a Python program to connect to an SQLite3 database, create a table, insert data, and
# fetch data.
# import sqlite3

# # 1. Connect to SQLite database (creates file if it doesn't exist)
# conn = sqlite3.connect("student.db")

# # 2. Create cursor object
# cur = conn.cursor()

# # 3. Create table
# cur.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER,
#     city TEXT
# )
# """)

# print("Table created successfully!")

# # 4. Insert data into table
# cur.execute("INSERT INTO students (name, age, city) VALUES ('Rahul', 21, 'Mumbai')")
# cur.execute("INSERT INTO students (name, age, city) VALUES ('Sneha', 22, 'Delhi')")
# cur.execute("INSERT INTO students (name, age, city) VALUES ('Amit', 20, 'Pune')")

# # Save changes
# conn.commit()
# print("Data inserted successfully!")

# # 5. Fetch and display data
# cur.execute("SELECT * FROM students")
# rows = cur.fetchall()

# print("\nFetching Data:")
# for row in rows:
#     print(row)

# # 6. Close connection
# conn.close()

# Write a Python program to create a database and a table using
# SQLite3
# import sqlite3

# connection = sqlite3.connect("college.db")
# cursor = connection.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     course TEXT
# )
# """)

# print("Database and Table created successfully!")

# connection.close()

# Write a Python program to insert data into an SQLite3 database and fetch it.
# import sqlite3

# conn = sqlite3.connect("student.db")
# cur = conn.cursor()

# cur.execute("INSERT INTO students (name, age, city) VALUES ('Riya', 19, 'Surat')")
# cur.execute("INSERT INTO students (name, age, city) VALUES ('Kunal', 20, 'Rajkot')")
# conn.commit()

# cur.execute("SELECT * FROM students")
# rows = cur.fetchall()

# for row in rows:
#     print(row)
            
# conn.close()

