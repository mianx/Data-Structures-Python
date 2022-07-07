def BinarySearch(lst,targetValue):
    #[1,2,4,5,6,7,8]
    midIndex = len(lst) // 2

    if lst[midIndex] == targetValue:
        return lst[midIndex]
    if lst[midIndex] > targetValue:
        BinarySearch(lst[:midIndex],targetValue)
    elif lst[midIndex] < targetValue:
        BinarySearch(lst[midIndex:],targetValue)

print(BinarySearch([1,2,4,5,6,7,8],4))
