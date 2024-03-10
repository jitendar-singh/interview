def length_dict(dict1):
    count = 0
    for keys in dict1:
        count+=1
    return count

dct = {'Sunny':34,'Monalisa':31,'Yuvraj':10, 'SaviRaj':5}
print(length_dict(dct))