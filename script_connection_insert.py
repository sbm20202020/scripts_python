import mysql.connector
from mysql.connector import Error


def insert_varibles_into_table(id, name, price, purchase_date):
    connection = mysql.connector.connect(host='172.17.0.1',
                                         database='db_inss',
                                         user='user',
                                         password='password',
                                         port='3340')
    try:
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """

        record = (id, name, price, purchase_date)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            
insert_varibles_into_table(2, 'Area 51M', 6999, '2019-04-14')
insert_varibles_into_table(3, 'MacBook Pro', 2499, '2019-06-20')
