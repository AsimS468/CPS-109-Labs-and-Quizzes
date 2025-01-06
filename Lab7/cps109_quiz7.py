#Name: Muhammad Asim Salman
#SID: 501177482
#Quiz 7: Recursive list length

def rlen(items):
    lenCount = 0
    if items == []:
        return lenCount
    lenCount = lenCount + 1
    return lenCount + rlen(items[1:])

l1 = [1]
l2 = [1,2]
l3 = [1, 2, 3, 4, 5 ,6]

print(rlen(l1))
print(rlen(l2))
print(rlen(l3))