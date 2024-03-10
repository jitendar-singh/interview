def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

result = factorial(3)
print(result) # Output: 120
