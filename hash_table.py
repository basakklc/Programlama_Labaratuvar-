#Hash tablosunda çakışma olup olmadığını bulan ve bu çakışmanın kaç kere olduğunu hesaplayan kod..

import random
def createMyHashTable(N):
    myTable=[]
    for i in range(N):
        myTable.append(0)
    return myTable


def my_hash(size,numberToBeInserted):
    return numberToBeInserted%size

def insertMyHashTable(myTable,numberToBeInserted):
    isCollision=False
    index=my_hash(len(myTable),numberToBeInserted)
    if(myTable[index]==0):
        myTable[index]=1
    else:
        isCollision=True
    return isCollision


m_h_1=createMyHashTable(5)
print(insertMyHashTable(m_h_1,20))
print(insertMyHashTable(m_h_1,20))



def myTest(size=13,numberToBeInserted=10):
    m_h_1=createMyHashTable(size)
    c=0
    for s in range(numberToBeInserted):
        number=random.randint(0,10000)
        if(insertMyHashTable(m_h_1,number)==True):
            c=c+1
    return c

print(myTest(700,50),"*")


