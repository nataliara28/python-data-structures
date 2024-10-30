# 1. Hobbies Tracker
# Add hobbies and display the unique hobbies list.

# Set is best data structure

#Initialize hobbies tracker
hobbies = set()

# Add hobbies
hobbies.add("reading")
hobbies.add("coding")
hobbies.add("reading") # Duplicated should not be added
hobbies.add("cycling")

# Output?
print(hobbies)



# 2. Phonebook Directory
# Create a phonebook, add a contact, and retrieve a phone number.

# Initialize dictionary phonebook
phonebook = {}

# Add contacts
phonebook['Alice'] = 345678987
phonebook['Jack'] = 697321445

print(phonebook)

# Retrieve Alice's phone
print(phonebook["Alice"])


# 3. Student Attendance List

# Add attendance entries and display the list

# Initialize a list
attendance = []

# Add attendance entrie
attendance.append('Alice')
attendance.append('Bob')
attendance.append('Jack')

print(attendance)

# 4. Grade Record
# Create a grade record for a student and print their details

# Initialise a tuple

student_grade= ('Alice', 85)

# Print - Display student details

print('Student', student_grade[0])
print('Grade', student_grade[1])