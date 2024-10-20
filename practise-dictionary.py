# Dictionary
# Second Most Commonly Used: Dictionaries are widely used when data needs to be accessed via a unique key 
# rather than a positional index.

# Reasons for Popularity:
# Allows for fast lookups, insertions, and deletions by key.
# Flexible in terms of the types of values that can be stored, making them suitable for mapping relationships.
# Often used for storing structured data such as configuration settings, JSON-like data, and records.

# Common Use Cases:
# Storing key-value pairs for quick access, like user profiles, settings, and caches.
# Representing objects with attributes in web applications or APIs.

# Syntax: dict_name = {key1: value1, key2: value2}

#Example

student = {"name": "Alice", "age": 22, "major": "Physics"}
print(student["name"]) 

# Add math grade
student["math_grade"] = 90
print(student)

# Delete "major"
del student["major"]


# Update math grade
student["math_grade"] = 95
print(student)