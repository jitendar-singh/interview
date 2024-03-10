# Write a Python program to iterate over a dictionary and print its keys and values.

def dict_iterator(dc):
    for key, value in dc.items():
        print(key,':',value)

dct = {'Sunny':34,'Monalisa':31,'Yuvraj':10}
dict_iterator(dct)