def sort_dict_value(dct):
    sorted_dict = dict(sorted(dct.items(), key=lambda x: x[1]))
    return sorted_dict




dct = {'Sunny':34,'Monalisa':31,'Yuvraj':10}
print(sort_dict_value(dct))
