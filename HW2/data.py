import mysql.connector
from mysql.connector import Error

# Function to get all data from users, products, and countries
def get_data(table_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ab271642",
            database="my_database",
            port=3307
        )
        cursor = connection.cursor(dictionary=True)
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Database connection error: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to insert data into a specific table
def insert_data(table_name, id, value):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ab271642",
            database="my_database",
            port=3307
        )
        cursor = connection.cursor()
        if table_name == 'users':
            sql = "INSERT INTO users (id, user_name) VALUES (%s, %s)"
        elif table_name == 'products':
            sql = "INSERT INTO products (id, product_name) VALUES (%s, %s)"
        else:
            sql = "INSERT INTO countries (id, country_name) VALUES (%s, %s)"
        cursor.execute(sql, (id, value))
        connection.commit()
    except Error as e:
        print(f"Insert error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to delete data from a specific table
def delete_data(table_name, id):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ab271642",
            database="my_database",
            port=3307
        )
        cursor = connection.cursor()
        sql = f"DELETE FROM {table_name} WHERE id = %s"
        cursor.execute(sql, (id,))
        connection.commit()
    except Error as e:
        print(f"Delete error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to join three tables on 'id'
def join_tables():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ab271642",
            database="my_database",
            port=3307
        )
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT users.id, users.user_name, products.product_name, countries.country_name
        FROM users
        JOIN products ON users.id = products.id
        JOIN countries ON users.id = countries.id
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Join query error: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
def update_data(table_name, id, value):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ab271642",
            database="my_database",
            port=3307
        )
        cursor = connection.cursor()
        if table_name == 'users':
            sql = "UPDATE users SET user_name = %s WHERE id = %s"
        elif table_name == 'products':
            sql = "UPDATE products SET product_name = %s WHERE id = %s"
        else:
            sql = "UPDATE countries SET country_name = %s WHERE id = %s"
        cursor.execute(sql, (value, id))
        connection.commit()
    except Error as e:
        print(f"Update error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

