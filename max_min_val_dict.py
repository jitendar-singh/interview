def min_max_val(dct):
    sorted_values = sorted(dct.items(),key= lambda x: x[1])
    return sorted_values[0][1], sorted_values[len(sorted_values)-1][1]

dct = {'Sunny':34,'Monalisa':31,'Yuvraj':10}
minimum_value, maximum_value = min_max_val(dct)
print(f'Minimum Value is {minimum_value} and Maximum Value is {maximum_value}')