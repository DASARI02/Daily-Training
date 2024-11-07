# Function to add a new product
def add_product(products, product_id, name, price):
    if product_id in products:
        print(f"Product with ID {product_id} already exists.")
    else:
        products[product_id] = {"name": name, "price": price}
        print(f"Product '{name}' added with ID {product_id}.")

# Function to list all products
def list_products(products):
    if not products:
        print("No products available.")
    else:
        for product_id, info in products.items():
            print(f"ID: {product_id}, Name: {info['name']}, Price: {info['price']}")

# Function to update product information
def update_product(products, product_id, name=None, price=None):
    if product_id not in products:
        print(f"Product with ID {product_id} does not exist.")
    else:
        if name:
            products[product_id]["name"] = name
        if price is not None:
            products[product_id]["price"] = price
        print(f"Product ID {product_id} updated.")

# Function to apply a discount to all products
def apply_discount(products, percentage):
    if percentage < 0 or percentage > 100:
        print("Please enter a valid percentage (0-100).")
        return
    for product_id, info in products.items():
        old_price = info["price"]
        discount_amount = old_price * (percentage / 100)
        info["price"] = round(old_price - discount_amount, 2)
    print(f"Applied {percentage}% discount to all products.")
