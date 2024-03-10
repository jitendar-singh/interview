'''Write a Python function that takes in a string and returns the count of each character in the string, sorted by descending count.
'''

def count_char(characters):
    count_table = {}
    for char in characters:
        if char in count_table:
            count_table[char]+=1
        else:
            count_table[char]=1
    sorted_char_count = sorted(count_table.items(),key= lambda x:x[1], reverse=True)
    return sorted_char_count

mystring = "hello world"
res = count_char(mystring)
print(res)