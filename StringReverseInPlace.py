def ReverseString(str):
    rang = len(str) // 2
    for i in range(rang):
        temp = str[i] 
        lastind = (i + 1) * -1
        str[i] = str[lastind]
        str[lastind] = temp

def reverse(list_of_chars):

    left_index  = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1

strr = ['a','b','d','i','o']
ReverseString(strr)
print(strr)
reverse(strr)
print(strr)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit('ReverseString(strr)', setup='from __main__ import ReverseString', globals=globals(),number=100))
    print(timeit.timeit('reverse(strr)', setup='from __main__ import ReverseString', globals=globals(),number=100))
    

