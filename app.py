from flask import Flask, jsonify
import json

app = Flask(__name__)

# Function to read data from JSON file
def read_data_from_file():
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return {"error": str(e)}

@app.route('/products', methods=['GET'])
def get_products():
    data = read_data_from_file()
    return jsonify(data)

@app.route('/products/<string:product_name>', methods=['GET'])
def get_product_by_name(product_name):
    data = read_data_from_file()
    product = next((item for item in data if item["name"] == product_name), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
