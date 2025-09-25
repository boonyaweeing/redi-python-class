# Alice goes to the store with a bag containing a pen.
thingsInBag = ["pen"]

# Alice buys a notebook and puts it in her bag.
thingsInBag.append("notebook")
# Alice buys a laptop and puts it in her bag.
thingsInBag.append("laptop")
# Alice buys a pencil and puts it in her bag.
thingsInBag.append("pencil")
# On the way home, Alice meets a friend and gives them the pen.
thingsInBag.remove("pen")
# But Alice then hesitate if she has enough room in her bag for another item. She checks.
print(len(thingsInBag))
# Alice find the number of items in her bag, and wants to remember if she has a laptop in her bag.
print(thingsInBag.index("laptop"))
# When Alice gets home, she takes all the items out of her bag and shows them to her family.
print(thingsInBag)


"""
append(element) → Adds an element at the end of the list
count(element) → Returns the number of elements with the specified value
index(element) → Returns the index of the first element with the specified value
insert(element) → Adds an element at the specified position
remove(element) → Removes the first item with the specified value
reverse() → Reverses the order of the list
sort() → Sorts the list

"""