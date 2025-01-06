#Name: Muhammad Asim Salman
#SID: 501177482
#Quiz 5: Faro Shuffle

def feroShuffle(boolVal, items):
    x = len(items)
    fHalf = items[:x//2]
    sHalf = items[x//2:]
    newList = []
    
    if boolVal:
        for i in range(len(fHalf)):
            newList.append(fHalf[i])
            newList.append(sHalf[i])
    else:
        for i in range(len(fHalf)):
            newList.append(sHalf[i])
            newList.append(fHalf[i])
    
    return newList

print("Is this an Out-Shuffle(True) or In-Shuffle(False)?")
b = input("Input a True or False: ").strip().lower() == "true"

llist = []
intt = int(input("Input the length of your list (even number please): "))
for j in range(intt):
    k = input("Input the a value in your list: ")
    llist.append(k)

result = feroShuffle(b, llist)
print("Shuffled list:", result)

    