def isbalanced(expn):
    stack = []
    openP = ['(', '[', '{']
    closeP = [')', ']', '}']

    for params in expn:
        if params in openP:
            stack.append(params)
        else:
            if not stack:
                return False
            flag = stack.pop()
            oflag = openP.index(flag)
            cflag = closeP.index(params)
            if oflag != cflag:
                return False
    if stack:
        return False
    else:
        return True

expn = '(({[]}[])[]()'
print(isbalanced(expn))