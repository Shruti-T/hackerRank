class HashTable:
    def __init__(self,size):
        self.size=size
        self.hashTable=self.creatBuckets()
    
    def creatBuckets(self):
        # return [[] for _ in range(self.size)]
        arr=[]
        for _ in range(self.size):
            arr.append([])
        return arr
    
    def setVal(self,key,val):
        #get index from key by hash function 
        hashedKey=hash(key)%self.size
        print(hashedKey,'iiiiii',hash(key))
        # get bucket corresponding to index
        bucket=self.hashTable[hashedKey]

        foundKey=False
        for index,record in enumerate(bucket):
            recordedKey,recordedVal=record
            # is bucket key and given key same??
            if(recordedKey==key):
                foundKey=True
                break
        # if key foung update.... else append
        if foundKey:
            bucket[index]=(key,val)
        else:
            bucket.append((key,val))
    
    def getVal(self,key):
        hashedKey=hash(key)%self.size
        bucket=self.hashTable[hashedKey]

        foundKey=False
        for index,record in enumerate(bucket):
            recordkey,recordVal=record

            if recordkey == key:
                foundKey=True
                break

        if foundKey:
            return recordVal
        else:
            return "No record found!!"
    
    def deleteVal(self,key):
        hashedKey=hash(key)%self.size
        bucket=self.hashTable[hashedKey]

        foundKey=False
        for index,record in enumerate(bucket):
            recordkey,recordVal=record

            if recordkey == key:
                foundKey=True
                break

        if foundKey:
            bucket.pop(index)
        returnhashedKey=hash(key)%self.size
        bucket=self.hashTable[hashedKey]

        foundKey=False
        for index,record in enumerate(bucket):
            recordkey,recordVal=record

            if recordkey == key:
                foundKey=True
                break

        if foundKey:
            return recordVal
        else:
            return "No record found!!"
    def __str__(self):
        return "".join(str(item) for item in self.hashTable)

hashTable=HashTable(50)

#inserting values

hashTable.setVal("value1","ShrutiTiwari")
print(hashTable)

hashTable.setVal("value2","Shaivy")
print(hashTable)

ans=hashTable.getVal("value2")
print(ans)

hashTable.deleteVal("value2")
print(hashTable)