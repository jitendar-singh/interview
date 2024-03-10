def remove_key_value(dct, key):
    return dct.pop(key)

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

removed_value = remove_key_value(my_dict, 'name')
print(removed_value)
print(my_dict)


