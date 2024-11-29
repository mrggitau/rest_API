
# REST API PROJECT

OKAY, THIS IS A REALLY SIMPLE REST API PROJECT THAT HANDLES PRODUCTS.

## FEATURES
- ADD PRODUCTS (POST /products)
- LIST ALL PRODUCTS (GET /products)

## SETUP INSTRUCTIONS

### 1. INSTALL PYTHON
- DOWNLOAD AND INSTALL PYTHON FROM [https://www.python.org/](https://www.python.org/).

### 2. INSTALL REQUIRED LIBRARIES
- OPEN YOUR TERMINAL AND RUN THESE COMMANDS:

```
pip install flask requests
```

### 3. RUN THE API SERVER
- OPEN A TERMINAL IN THIS PROJECT FOLDER AND TYPE:
```
python app.py
```

### 4. TEST THE API
- USE POSTMAN OR THE client.py SCRIPT TO TEST IT.

#### EXAMPLES:
- TO ADD A PRODUCT, USE:
```
POST http://127.0.0.1:5000/products
BODY:
{
    "name": "Tablet",
    "description": "A cool tablet",
    "price": 499.99
}
```

- TO LIST PRODUCTS, USE:
```
GET http://127.0.0.1:5000/products
```
