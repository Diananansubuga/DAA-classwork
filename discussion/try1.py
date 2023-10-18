def binary_search(list,target):
    first=0
    last=len(list)-1

    while first<=last:
        midpoint=(first+last)//2
        if list[midpoint]==target:
            return midpoint
        elif list[midpoint]<target:
            first=midpoint+1

        else:
            last=midpoint-1

    return None

def verify(num):
    if num is not None:
        print("element is in the list at", num)

    else:
        ("print target not found: ")


numbers=[1,2,3,4,5,6,7]
binary_search(numbers,6)
verify(binary_search(numbers,6))

            
