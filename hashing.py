from sys import hash_info


class hashTable():
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]
    
    def getHash(self, key):
        h = 0
        for chr in key:
          h += ord(chr)
        return h % self.Max

    def __setitem__(self,key,value):
        index = self.getHash(key)
        self.arr[index] = value

    def __getitem__(self,key):
        index = self.getHash(key)
        return self.arr[index]
h = hashTable()
h['ali'] = 20
print(h['ali'])
