'''Write a Python function that takes in a list of strings and returns 
a new list containing only the strings that start with a capital letter.'''

def filter_strings(strings):
    new_list = []
    for items in strings:
        if items[0].isupper():
            new_list.append(items)
    return new_list

string_list = ["sunny", "Sunny", "Runny", "sAndip", "monalisa", "Sony"]
new_list = filter_strings(string_list)
print(new_list)