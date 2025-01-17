import sqlite3

def create_table():
    conn = sqlite3.connect('employee_db')
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE if not exists  employee (
            id text PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            salary REAL NOT NULL,
        )'''
    )