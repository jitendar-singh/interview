def merge_dicts(dct1,dct2):
    merged_dict = dct1.copy()
    merged_dict.update(dct2)
    return merged_dict

dict1 = {'name': 'John', 'age': 30}
dict2 = {'city': 'New York', 'country': 'USA'}

# Merge dictionaries
merged_dict = merge_dicts(dict1, dict2)

# Print the merged dictionary
print(merged_dict)