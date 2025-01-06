def iscyclops(n):
    numStr = str(n)
    x = len(numStr)

    if x%2 != 0:
        if x == 1 and numStr[0]:
            return True
        elif numStr[int(x/2)] == 0:
            return True
        return False
    return False
    
print(iscyclops(0))