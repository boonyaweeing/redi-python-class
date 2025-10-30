"""

filepath = "./08/tryout.txt"
for i in range(4):  
    with open(filepath, 'r') as infile:
        content = infile.read()
    print(content)

"""
"""
filepath = "./exercise1.txt"
lines = []
for i in range(2):  
    line = input(f"Please enter line {i+1} of the text:")
    lines.append(line)

with open(filepath, 'w') as file:
    content = file.write(str(lines))
file.close()
with open(filepath, 'r') as file:
    content = file.read()
print(content)
"""



