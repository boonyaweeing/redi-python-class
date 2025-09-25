alicesPreferences = {
    "color": "red",
    "numOfDoors": 4
    }

bobsPreferences = {
    "brand": "BMW",
    "isSunProof": True
}

alicesPreferences.update(bobsPreferences)

alicesPreferences["price"] = 200000

alicesPreferences.pop("brand")

alicesPreferences["price"] = 180000

print(alicesPreferences)

"""
Dictionary methods:
clear() → Removes all key-value pairs from the dictionary.
get(key, default=None) → Returns the value for a key, or a default if the key is not found.
keys() → Returns a list-like view of all keys.
values() → Returns a list-like view of all values.
items() → Returns a list-like view of key-value pairs as tuples.
pop(key, default=None) → Removes and returns the value of a key, or returns default if the key is missing.
update(dict2) → Adds or updates key-value pairs from another dictionary.

"""