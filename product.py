# Write a Python function that takes in a list of integers and returns the largest product that can be made by multiplying 
# any three integers in the list.

# For example, given the input list [1, 2, 3, 4, 5], the function should return 60, which is the result of multiplying 
# 4, 5, and 3.

# Note that the input list may contain negative numbers, and you should handle those cases appropriately.
#  Also, the function should handle lists of any length, but you can assume that the input list will contain at least three integers.

def largest_product(mylist)-> int():
    product = 1
    mylist.sort()
    for items in mylist[-3:]:
        product*=items
    return product


mylist = [1,5,3,4,2]
print(largest_product(mylist))


    