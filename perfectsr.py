def utils(num):
    if num == 1:
        return True
    s = 1
    e = num//2
    

    while s <= e:
        m = (s+e)//2
        if m**2 == num:
            return True
        elif m**2 > num:
            e = m - 1
        else:
            s = m + 1
    return False
# s = 1 e = 13+1//2 = 7
# m = 1+7//2 = 4 4 ** 2 = 16
# 16 > num ? e = m -1 (3), s = 1
# m = 1+3//2 = 2 2**2 = 4
num = -1
print(utils(num))