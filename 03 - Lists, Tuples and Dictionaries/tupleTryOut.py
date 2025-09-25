"""list_coordinates = [1,2,3,4,5,6,7,8]
listoftuples = []
# I go through the list of coordinates
# and every pair in the list is added to a tuple and appended to the list of tuples"""


list_coordinates = [1, 2, 3, 4, 5, 6, 7, 8]
listoftuples = []

# Go through the list two items at a time
for i in range(0, len(list_coordinates), 2):
    pair = (list_coordinates[i], list_coordinates[i + 1])
    listoftuples.append(pair)

print(listoftuples)


