def ReverseString(str):
    rang = len(str) // 2
    for i in range(rang):
        temp = str[i] 
        lastind = (i + 1) * -1
        str[i] = str[lastind]
        str[lastind] = temp

strr = ['a','b','d','i','o']
ReverseString(strr)
print(strr)
