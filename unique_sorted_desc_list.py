'''
Write a Python function that takes in a list of integers and returns a new list containing the same elements as the original list,
 but sorted in descending order, with duplicates removed.
'''

def filter_list(myList):
    new_list = list(set(myList))
    new_list.sort(reverse=True)
    return new_list


myList = [3,1,6,1,7,2,3,5,6,7,1,3]
myNewList = filter_list(myList)
print(myNewList)