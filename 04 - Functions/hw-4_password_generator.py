"""
# Password Generator - Practical Functions Exercise

## Problem
You need to create a secure password generator for a company's IT department. 
Different departments have different password requirements, and the tool needs to be flexible and reusable.

## Requirements
Create a password generator that can:

1. **Generate different types of passwords:**
   - Simple (letters only)
   - Standard (letters + numbers)
   - Strong (letters + numbers + symbols)
   - Ultra-secure (all characters with specific requirements)

2. **Validate password strength:**
   - Check length requirements
   - Verify character type requirements
   - Calculate strength score

3. **Batch generation:**
   - Generate multiple passwords at once
   - Allow customization of requirements

## Expected Behavior
```
Password Generator
=================

1. Generate Single Password
2. Generate Multiple Passwords
3. Check Password Strength
4. Exit

Choose an option: 1

Password Types:
1. Simple (letters only)
2. Standard (letters + numbers)  
3. Strong (letters + numbers + symbols)
4. Ultra-secure (all types + requirements)

Choose password type: 3
Enter password length (8-50): 12

Generated Password: Kp9$mN2@vX8!
Password Strength: Strong (Score: 85/100)

Would you like another password? (y/n): n
```

## Real-World Value
This exercise demonstrates functions in a practical context where:
- Code reusability is essential (different password types)
- Validation logic is complex but reusable
- The main program logic stays clean and focused
- Functions make testing and maintenance easier

## Hints
Consider functions for:
- Generating different character sets
- Creating passwords with specific rules
- Validating password requirements
- Calculating strength scores
- Formatting output
- Menu handling

"""

import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "{", "}", "[", "]", "|", ";", "'", '"', "<", ">", ".", "?", "/"]

exit = False
def simple(length):
    password = ""
    for i in range (int(length)):
        random_letter = random.choice(letters) #random.choice() selects one random item from a sequence (like a list, tuple, or string).
        password += random_letter
    strength_score = 50
    return password

def standard(length):
    combined_list = letters + numbers
    password = ""
    for i in range (int(length)):
        random_character = random.choice(combined_list)
        password += random_character
    strength_score = 60
    return password

def strong(length):
    combined_list = letters + numbers + symbols
    password = ""
    for i in range (int(length)):
        random_character = random.choice(combined_list)
        password += random_character
    strength_score = 80
    return password

def secure(length):
    combined_list = letters + numbers + symbols
    password = ""

    if int(length) >= 10:
        for i in range (int(length)):
            random_character = random.choice(combined_list)
            password += random_character
        strength_score = 90
        return password
    else:
        print("The length of password(s) should be at least 10!!")
        secure(int(input("Please re-enter the length of password(s): ")))
        return None
    

def many_passwords(amount, type, length):
    passwords = []
    for i in range (int(amount)):
        if type == "1":
            passwords.append(simple(length))
        elif type == "2":
            passwords.append(standard(length))
        elif type == "3":
            passwords.append(strong(length))
        elif type == "4":
            passwords.append(secure(length))
        
    for password in passwords:
        print("\n" + f"Generated Password: {password}")

def exit_program():
    answer = input("\n" + "Would you like another password? (y/n): ")
    if answer == "y":
        exit = False
    else:
        exit = True


def generate_password(option, password_type, password_length):
    if option == "1":
        if password_type == "1":
            generated_password = simple(password_length)
        elif password_type == "2":
            generated_password = (standard(password_length))
        elif password_type == "3":
            generated_password = (strong(password_length))
        elif password_type == "4":
            generated_password = (secure(password_length))
    
        print("\n" + f"Generated Password: {generated_password}")

    elif option == "2": 
        amount = input("How many passwords do you want to generate?: ")
        many_passwords(amount, password_type, password_length)
    elif option == "3": 
        print("Sorry, this feature is NOT available at the moment. :(")
   


def initiate():
    print("Password Generator")
    print("=================" + "\n")
    print("1. Generate Single Password"+ "\n" +
        "2. Generate Multiple Passwords"+ "\n" +
        "3. Check Password Strength"+ "\n" +
        "4. Exit"+ "\n")

    option = input("Choose one option: ")

    if option != "4":
        
        print("\n" + "Password Types:" + "\n" +
        "1. Simple (letters only)" + "\n" +
        "2. Standard (letters + numbers)" + "\n" +  
        "3. Strong (letters + numbers + symbols)" + "\n" +
        "4. Ultra-secure (all types + requirements)" + "\n")

        password_type = input("Choose password type: ")
        password_length = input("Enter password length (8-50): ")
        generate_password(option, password_type, password_length)





while exit == False:
    initiate()
    answer = input("\n" + "Would you like another password? (y/n): ")
    if answer == "y":
        exit = False
    else:
        exit = True
 
print("---Program ended---")
