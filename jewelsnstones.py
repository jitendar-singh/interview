def utils(j, s):
    count = 0
    jewels_set = set()
    for jewels in j:
        jewels_set.add(jewels)
    
    for stone in s:
        if stone in jewels_set:
            count+=1
    return count

jewels = 'd'
stones = 'aAAbbbbc'
print(utils(jewels, stones))