supermarket_products = {
    "Milk": 1.99,
    "Eggs": 3.49,
    "Bread": 2.49,
    "Bananas": 0.69,
    "Chicken": 5.99
}

def add_product(products_list, product, price):
    # TODO Raise MemoryError error if product name is too large (> 100 chars)
    if len(product) > 100:
        raise MemoryError("Product name is too large.")

    # TODO Convert price to float
    price = float(price)

    # Add element to list
    products_list[product] = price
    # Print message
    print(f"{product} added with price of {price}")
    return products_list


while True:
    print(f"\n{'-' * 50}")
    option = input("Welcome, select one of the following options:\n\t1 Retrieve price\n\t2 Add product\n")
    # Retrieve price
    if option == "1":
        product = input("Enter product name: ")
        # TODO Try to get price (catch potential exceptions)
        try:
            price = supermarket_products[product]
            print(f"The price of {product} is: {price}")
        except:
            print(f"Product {product} not found.")





    # Add new product
    elif option == "2":
        product = input("Enter new product name: ")
        price = input("Enter price: ")
        # TODO Try to add the product (catch potential exceptions)
        try:
            add_product(supermarket_products,product, price)
            print(f"Product {product} with price {price} was added.")
        except:
            print(f"Product {product} with price {price} could not be added.")





    # Invalid option
    else:
        print("Invalid option")
