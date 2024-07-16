import requests

# To get all products
response = requests.get('http://127.0.0.1:5000/products')
print("Tüm Ürünler:", response.json())

# To get a specific product by namen
product_name = "ExampleProductName"  # Write the actual product name here
response = requests.get(f'http://127.0.0.1:5000/products/{product_name}')
print(f"Ürün '{product_name}':", response.json())
