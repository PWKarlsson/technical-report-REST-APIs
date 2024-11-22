from flask import Flask, request, jsonify

app = Flask(__name__)

items = [{'id': 1, 'name': 'Item 1'}]


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


@app.route('/items', methods=['POST'])
def add_item():
    new_item = {'id': len(items) + 1, 'name': request.json['name']}
    items.append(new_item)
    return jsonify(new_item), 201


if __name__ == '__main__':
    app.run(debug=True)
