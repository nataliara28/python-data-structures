# List
# Most Commonly Used: Lists are the most frequently used data structure in Python because of their flexibility, 
# ease of use, and built-in functionality.

# Reasons for Popularity:
# Can store any type of data, including mixed types (integers, strings, other lists).
# Supports dynamic resizing, making it easy to add, remove, or modify elements.
# Offers a variety of built-in methods for sorting, searching, and manipulating data.

# Common Use Cases:
# Storing a sequence of elements in a specific order (e.g., user inputs, data from files, processing loops).
# Iterating over items, filtering lists, or applying functions to elements.

# Syntax: list_name = [element1, element2, element3]

# Example

fruits = ["apple", "banana", "cherry"]
print(fruits[0])

# Add a fruit
fruits.append('orange')

# Delete a fruit
fruits.remove('banana')

# Add a fruit in index 1
fruits.insert(1, 'grape')
print(fruits)

# Update the fruit index 2
fruits[2] = 'mango'
print(fruits)



# movies example
movies = ["Inception", "The Matrix", "Interstellar", "The Godfather", "Parasite"]

# Access first movie
movies[0]

# Access last movie
movies[-1]

# Add a movie
movies.append("Avengers")

# update a movie
movies[1] = 'Titanic'


# Nested list

nested_list = [
    1, 
    2, 
    [], 
    ['a', 'b', 'c'], 
    {'a': 'c'}, 
    [3, 4, [5, 6], {'key1': 'value1', 'key2': [7, 8]}]
]

# Accessing the third element (['a', 'b', 'c']):
third_element = nested_list[3]
print(third_element)

# Accessing the dictionary ({'a': 'c'}) and getting the value for key 'a':
dict_value = nested_list[4]['a']

# Accessing the nested list inside the last element ([5, 6]):
nested_sublist = nested_list[5][2]

# Accessing the value associated with 'key2' inside the nested dictionary:
key2_value = nested_list[-1][-1]['key2']
print('key2_value', key2_value)


nested_list = [
    1, 
    2, 
    [], 
    ['a', 'b', 'c'], 
    {'a': 'c'}, 
    [3, 4, [5, 6], {'key1': 'value1', 'key2': [7, 8]}]
]

# Looping through

for sublist in nested_list:
    # print('level 1: ')
    
    # if it's a list, traverse its elements
    if type(sublist) is list:
        for item in sublist:
            if type(item) is list:
                print('     level 2 - nested list :', item)
            elif type(item) is dict:
                print('     level 2 - dictionary: ', item)
            else:
                print(f"       level 2: {item}")
            
    # if it's a dictionary
    elif type(sublist) is dict:
        print('level 1:')
        for key, value in sublist.items():
            print(f"    {key}: {value}")
            
    # for non-list, non dictionary values
    else:
        print(sublist)
            
    
