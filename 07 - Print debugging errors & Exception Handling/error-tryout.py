"""
exit = False

while not exit:
    print("not exiting")
    foo = input("Enter 'exit' to exit: ")
    if foo == "exit":
        exit = True

print(exit)
print("--exitted--")
"""

apple_products = {
    "iPhone 17 Pro": 1200,
    "MacBook Pro M4": 2000,
}

while True:
    # Get user input
    product = input("Enter the product name: ")
    # Break if enter
    if product == "":
        break
    # Get price. Throws KeyError if product not in list
    try:
        price = apple_products[product]
        print(f"The price of {product} is: {price}")
    except:
        print(f"Product {product} not found.")
    #price = apple_products[product]

    #print(f"The price of {product} is: {price}")