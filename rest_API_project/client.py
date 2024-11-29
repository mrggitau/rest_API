
import requests

# THIS IS THE BASE URL WHERE OUR API IS RUNNING LOCALLY.
BASE_URL = "http://127.0.0.1:5000/products"

# FUNCTION TO ADD A NEW PRODUCT.
def add_product(name, description, price):
    # JSON DATA FOR THE NEW PRODUCT.
    data = {"name": name, "description": description, "price": price}
    
    # POST REQUEST TO ADD THE PRODUCT.
    response = requests.post(BASE_URL, json=data)
    
    # PRINT THE RESPONSE.
    print("ADD PRODUCT RESPONSE:", response.json())

# FUNCTION TO LIST ALL PRODUCTS.
def list_products():
    # GET REQUEST TO FETCH ALL PRODUCTS.
    response = requests.get(BASE_URL)
    
    # PRINT THE LIST OF PRODUCTS.
    print("PRODUCTS LIST:", response.json())

# THIS IS WHERE THE SCRIPT RUNS.
if __name__ == '__main__':
    # ADD A SAMPLE PRODUCT.
    add_product("Smartphone", "A fancy new smartphone", 899.99)
    
    # GET ALL PRODUCTS TO SEE IF IT WORKED.
    list_products()
