from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)
data_file = 'data.json'

# Đường dẫn đến tệp JSON
def read_data():
    if not os.path.exists(data_file):
        return []
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_data(data):
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    links = read_data()
    return render_template('index.html', links=links)

@app.route('/links', methods=['GET', 'POST'])
def manage_links():
    if request.method == 'POST':
        new_link = request.get_json()
        links = read_data()
        links.append(new_link)
        write_data(links)
        return jsonify(new_link), 201
    else:
        links = read_data()
        return jsonify(links)

if __name__ == '__main__':
    app.run(debug=True)
