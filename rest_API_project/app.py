
from flask import Flask, request, jsonify

# OKAY, SO THIS IS THE MAIN FILE TO RUN THE SERVER.
# WE USE FLASK TO HANDLE REQUESTS AND RESPONSES.

app = Flask(__name__)

# THIS LIST IS LIKE A DATABASE. IT JUST HOLDS OUR PRODUCTS.
products = []

# THIS ENDPOINT IS FOR CREATING A NEW PRODUCT.
@app.route('/products', methods=['POST'])
def create_product():
    # GRAB THE DATA FROM THE REQUEST.
    data = request.get_json()
    
    # CHECK IF ALL THE FIELDS EXIST. IF NOT, THROW AN ERROR.
    if not data or not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({'error': 'BRO, SOMETHING IS MISSING. YOU NEED name, description, AND price.'}), 400
    
    # ADD THE PRODUCT TO THE LIST.
    products.append(data)
    return jsonify({'message': 'YAY! PRODUCT CREATED!'}), 201

# THIS ENDPOINT IS FOR GETTING ALL THE PRODUCTS.
@app.route('/products', methods=['GET'])
def list_products():
    return jsonify(products), 200

# RUN THE SERVER. USE THIS COMMAND TO START IT.
if __name__ == '__main__':
    app.run(debug=True)
