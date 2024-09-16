from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Connect to the database and fetch data
def get_data():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_database",
            port=3307
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sample_table")
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Database connection error: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_data(name, age, city):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_database",
            port=3307
        )
        cursor = connection.cursor()
        
        # Corrected query using %s for all placeholders
        sql = "INSERT INTO sample_table (name, age, city) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, age, city))
        
        connection.commit()  # Commit the transaction to save the data
    except Error as e:
        print(f"Insert error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Update existing record
def update_data(id, name, age, city):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_database",
            port=3307
        )
        cursor = connection.cursor()
        sql = "UPDATE sample_table SET name=%s, age=%s, city=%s WHERE id=%s"
        cursor.execute(sql, (name, age, city, id))
        connection.commit()
    except Error as e:
        print(f"Update error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Delete a record
def delete_data(id):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_database",
            port=3307
        )
        cursor = connection.cursor()
        sql = "DELETE FROM sample_table WHERE id=%s"
        cursor.execute(sql, (id,))
        connection.commit()
    except Error as e:
        print(f"Delete error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Routes
@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = int(request.form['age'])
    city = request.form['city']
    insert_data(name, age, city)
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    age = int(request.form['age'])
    city = request.form['city']
    update_data(id, name, age, city)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    delete_data(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
