"""

List: Write a program that will use a while loop to obtain a set of numbers from the user.
When the user enters an 'x' or an 'X', sum the numbers and display both the sum and
the average of their numbers.

"""

user_input  = input("Please enter a set of number: ")

numbers = []

while user_input.lower() != "x":
    number = float(user_input)
    numbers.append(number)
    user_input  = input("Please enter the next number: ")

sum = 0
for i in numbers:
    sum += i

average = sum / len(numbers)

print(f"The sum of the input : {numbers} is {sum} and the avarage is {average}")