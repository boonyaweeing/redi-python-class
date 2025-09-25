"""
Dictionary: Write a program that will ask the user for a number and then calculate all the
squares from 1 to their number and store them in a dictionary. Print out the dictionary at
the end to see the results.
"""
squares = {}

input_num = int(input("Please enter a number: "))

for i in range(1, input_num + 1):
    squares[i] = i ** 2

print(f"squares from 1 to {input_num} : {squares}")