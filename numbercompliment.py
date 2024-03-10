def findComplement(num):
    i = 1
    while i <= num:
        num ^= i
        i <<= 1
    return num
print(findComplement(5))