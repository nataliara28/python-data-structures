# Set
# Fourth Most Commonly Used: Sets are less frequently used but are still valuable in specific scenarios where uniqueness matters.

# Reasons for Popularity:
# Automatically handles duplicates, making it ideal for membership testing.
# Supports mathematical set operations like union, intersection, and difference.
# Useful for deduplicating lists or performing fast membership checks.
#
# Common Use Cases:
# Finding unique elements in a collection.
# Performing set operations like intersection between two data sets.
# Implementing membership checks (e.g., checking for banned words or blacklisted users).

# Syntax: set_name = {element1, element2, element3}

# Example

unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers) # What would be the output?

# add a new number
unique_numbers.add(4)

# delete an existing number
unique_numbers.pop()


# new set
colors = {"red", "blue", "green"}

print(colors)
print(type(colors))

#1.  add a color
colors.add('yellow')

#2. add a color that is already in set and print what happens
colors.add('blue')
print(colors)

#3. Remove a color
colors.remove('red')

#4. Remove all colors
colors.clear()

# Perform a union operation between two sets of colors and print the result.

more_colors = {'black', 'green', 'white'}

all_colors = colors.union(more_colors)

print(all_colors)
