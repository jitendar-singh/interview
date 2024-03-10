# How do you check if a key exists in a dictionary in Python? Provide an example.

def search_key(dct,target):
    for key in dct.keys():
        if key == target:
            return True
    return False

dct = {'Sunny':34,'Monalisa':31,'Yuvraj':10}
target = 'Yuvraj'
isPresent = search_key(dct, target)
print(f'Searching {target} in dict, the result is {isPresent}')
