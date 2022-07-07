def selectSort(lst : list): 
    for i in range(len(lst)):
        min = i
        for j in range(i,len(lst)):
            if lst[j] < lst[min]:
                min = j
        lst[i],lst[min] = lst[min],lst[i]

lst = [92,54,12,54,3,67,18,33,1032,12321,89323,5,3,5,2,1]
selectSort(lst)
print(lst)