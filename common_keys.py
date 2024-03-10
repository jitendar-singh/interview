def common_keys(dict1, dict2):
    common_key = set(dict1.keys()) & set(dict2.keys())
    return common_key





dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
dict2 = {'age': 30, 'city': 'Chicago', 'country': 'USA'}

c_keys = common_keys(dict1,dict2)
print(c_keys)