import mysql.connector
mysqldb = mysql.connector.connect(host='localhost', user='root', password='', database='testdataset')
mysqlcursor = mysqldb.cursor()

#  SQL to create a table
# mysqlcursor.execute("create table studentrecord(rollnum INT, name VARCHAR(255), marks INT)")

# try:
#     # SQL to  insert data  into the table
#     mysqlcursor.execute("insert into studentrecord(rollnum, name, marks) values(4, 'Johny', 80)")
#     mysqldb.commit()
#     print("Record inserted  successfully")
# except:
#     mysqldb.rollback()

# display the record
try:
    mysqlcursor.execute("select * from studentrecord where  rollnum = 1")
    rows = mysqlcursor.fetchall()
    for i in rows:
        roll = i[0]
        name = i[1]
        marks = i[2]
        print(f"{roll}, {name}, {marks}")
except:
    print("Error in fetching data!")
    
mysqldb.close()