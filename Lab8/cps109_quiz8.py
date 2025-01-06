#Name: Muhammad Asim Salman
#SID: 501177482
#Quiz 8:
def next_item(items):
    try:
        return next(items)
    except StopIteration:
        return None


list_ = iter([1,2,3,4,5,6,7,8,9,10])
for i in range(11):
    print(next_item(list_))