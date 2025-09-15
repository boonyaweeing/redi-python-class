userInput = input("Please enter a string: ")


while userInput != "":
    print("First letter capitalized: ", userInput.capitalize())
    print("All lowercase:            ", userInput.lower())
    print("Title case:               ", userInput.title())
    print("All uppercase:            ", userInput.upper())
    userInput = input("Please enter a string: ")

print("Thanks for playing!")