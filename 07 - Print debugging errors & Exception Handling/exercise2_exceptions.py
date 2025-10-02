# Students MUST NOT change this map
data = {
    "name": "Ali",
    "age": "twenty",
    "numbers": [1, 2],
    "divisor": 0
}

def process_data(d):
    # 1) Accessing missing key
    #city = d["city"]
    try:
        city = d["city"]
    except:
        print(f"Accessing missing key")


    # 2) Wrong type conversion
    #age = int(d["age"])
    try:
        age = int(d["age"])
    except:
        print(f"Wrong type conversion")
    # 3) Index out of range
    #third_number = d["numbers"][2]
    try:
        third_number = d["numbers"][2]
    except:
        print(f"Index out of range")
    # 4) Division by zero
    #result = 10 / d["divisor"]
    try:
        result = 10 / d["divisor"]
        print("Result is:", result)
    except:
        print(f"Division by zero")
   


process_data(data)

print("Program finished successfully!")