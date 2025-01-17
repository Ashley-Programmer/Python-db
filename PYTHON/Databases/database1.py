import sqlite3

def create_table():
    connection = sqlite3.connect('EmployeeDB')
    cursor = connection.cursor()
    
    cursor.execute('''
                   CREATE TABLE if not exists Employees(
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   role TEXT,
                   gender TEXT,
                   status TEXT)''')
    
    connection.commit()
    connection.close()
    
    def fetch_employee():
        connection = sqlite3.connect('EmployeeDB')
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM Employees')
        
        employees = cursor.fetchall()
        connection.close()
        return employees
    
    def insert_employee(id, name, role, gender, status):
        connection = sqlite3.connect("EmployeeDB")
        cursor = connection.cursor()
        
        cursor.execute('INSERT INTO Employees (id, name, role, gender, status) VALUES (?, ?, ?, ?, ?)',
                       (id, name, role, gender, status))
        connection.commit()
        connection.close()
        
        
    def delete_employee(id):
        connection = sqlite3.connect("EmployeeDB")
        cursor = connection.cursor()
        
        cursor.execute('DELETE FROM Employees where id = ?', (id,))
        
        connection.commit()
        connection.close()
        
        
    def update_employee(new_name, new_role, new_gender, new_status, id):
        connection = sqlite3.connect("EmployeeDB")
        cursor = connection.cursor()
        
        cursor.execute("UPDATE Employees SET name = ?, role = ?, gender = ?, status = ? WHERE id = ?",
                       (new_name, new_role, new_gender, new_status, id))
        
        connection.commit()
        connection.close()
        
        
    def id_exists(id):
        connection = sqlite3.connect("EmployeeDB")
        cursor = connection.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM Employees where id = ?', (id,))
        
        result = cursor.fetchone()
        connection.close()
        return result[0] > 0
    
create_table()
