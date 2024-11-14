from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# 連線到 MongoDB
client = MongoClient("mongodb://localhost:27017/")  # 確認 MongoDB URL
db = client['database']                             # 資料庫名稱
collection = db['collection']                       # 集合名稱

# 顯示所有資料
@app.route('/')
def index():
    data = list(collection.find())
    for item in data:
        item['_id'] = str(item['_id'])  # 將 ObjectId 轉為字串，便於前端顯示
    return render_template('index.html', data=data)

# 新增資料
@app.route('/add', methods=['POST'])
def add_data():
    name = request.form.get('name')
    age = request.form.get('age')
    occupation = request.form.get('occupation')
    
    new_data = {"name": name, "age": int(age), "occupation": occupation}
    collection.insert_one(new_data)
    
    return redirect(url_for('index'))

# 刪除資料
@app.route('/delete/<id>', methods=['POST'])
def delete_data(id):
    collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

# 更新資料
@app.route('/edit/<id>', methods=['POST'])
def edit_data(id):
    name = request.form.get('name')
    age = request.form.get('age')
    occupation = request.form.get('occupation')

    updated_data = {"name": name, "age": int(age), "occupation": occupation}
    collection.update_one({'_id': ObjectId(id)}, {'$set': updated_data})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
