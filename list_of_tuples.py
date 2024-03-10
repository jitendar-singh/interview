# Write a Python function that takes in a list of tuples, 
# where each tuple contains a name and an age, and returns the names of the oldest people in the list.

def filter_data(people):
    max_age = 0
    oldest_person = ""
    for person in people:
        name, age = person
        if age > max_age:
            max_age = age
            oldest_person = person
    return oldest_person

people = [("Alice", 25), ("Bob", 3000), ("Charlie", 200)]
print(filter_data(people))
