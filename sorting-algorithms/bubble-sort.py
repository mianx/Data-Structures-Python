def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0,len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j],array[j+1] = array[j+1],array[j]

lst = [92,54,12,54,3,67,18,33,1032,12321,89323,5,3,5,2,1]
bubbleSort(lst)
print(lst)