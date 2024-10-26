from flask import Flask, render_template, request, redirect, url_for
from data import get_data, insert_data, delete_data, join_tables, update_data

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    users = get_data("users")
    products = get_data("products")
    countries = get_data("countries")
    return render_template('index.html', users=users, products=products, countries=countries)

@app.route('/add', methods=['POST'])
def add():
    table_name = request.form['table']
    id = request.form['id']
    value = request.form['value']
    insert_data(table_name, id, value)
    return redirect(url_for('index'))

@app.route('/delete/<table>/<int:id>',methods=['POST'])
def delete(table, id):
    delete_data(table, id)
    return redirect(url_for('index'))

@app.route('/join')
def show_join():
    joined_data = join_tables()  # 获取 JOIN 查询结果
    return render_template('join_results.html', data=joined_data)

@app.route('/update/<table>/<int:id>', methods=['POST'])
def update(table, id):
    value = request.form['value']
    update_data(table, id, value)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
