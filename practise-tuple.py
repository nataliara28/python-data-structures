# Tuple
# Third Most Commonly Used: Tuples are less commonly used than lists and dictionaries but still 
# play an important role when immutability is needed.

# Reasons for Popularity:
# Provides a way to store data that should not be changed after creation.
# Used frequently as return types for functions that return multiple values.
# More memory-efficient than lists due to their immutability.

# Common Use Cases:
# Storing fixed collections of related data, such as coordinates or date and time values.
# Grouping multiple return values from a function.
# Using as keys in dictionaries (since tuples are hashable, unlike lists).

# Syntax: tuple_name = (element1, element2, element3)

# Example

coordinates = (10, 20)
print(coordinates[1])






# Initial tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)



# Iterating through a tuple (looping through elements)
for item in my_tuple:
    print(item)
    
for item, index in enumerate(my_tuple):
    print(f"Index {index}: {item}")
    
    
# Nested tuples 
nested_tuple = (1, 2, (3, 4, 5), (6, 7, 8))

# Accessing the third element
print(nested_tuple[2])

# accessing the second element inside the nested tuple, 4
print(nested_tuple[2][1])

# accessing the second element inside the nested tuple, 8
print(nested_tuple[3][2])
print(nested_tuple[-1][-1])


# Outer loop to iterate through each element in the top-level tuple
nested_tuple = (1, 2, (3, 4, 5), (6, 7, 8))

for element in nested_tuple:
    # check if the element is a tuple itself 
    if type(element) is tuple: # is this true?
        print("Nested tuple found: ")
        # Inner loop to iterate through the nested tuple
        for inner_element in element:
            print(f'    Inner element: {inner_element}')
    else:
        # Print the non-tuple elements
        print(f"Outer element: {element}")
