def merge_dicts(dict1, dict2):
    print(f'dict1 {dict1}')
    print(f'dict2 {dict2}')
    for key, value in dict2.items():
        dict1[key] = value
    print(f'post merge dict1 {dict1}')

dict1 = {'name': 'John', 'age': 30}
dict2 = {'city': 'New York', 'country': 'USA'}

# Merge dictionaries
merge_dicts(dict1, dict2)