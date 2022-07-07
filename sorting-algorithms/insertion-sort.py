def insertSort(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i - 1
        while((j>=0) and (lst[j]) > key):
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = key

lst = [92,54,12,54,3,67,18,33,1032,12321,89323,5,3,5,2,1]

if __name__ == '__main__':
    import timeit
    print(timeit.timeit('insertSort(lst)', setup='from __main__ import insertSort', globals=globals(),number=100))