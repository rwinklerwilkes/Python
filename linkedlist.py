class LinkedList:
    def __init__(self,data):
        self.head = Node(data,None)
    def insert(self, data):
        x = self.head
        while x is not None:
            prev = x
            x = x.nNode
        prev.nNode = Node(data,None)
    def traverse(self):
        x = self.head
        while x is not None:
            print(x.data)
            x = x.nNode
    def search(self, value):
        x = self.head
        while x is not None and x.data != value:
            x = x.nNode
        return x
    def delete(self, value):
        x = self.head
        while x is not None and x.data != value:
            prev = x
            x = x.nNode
        if x is not None:
            prev.nNode = x.nNode
        else:
            return "Could not find value"

class Node:
    def __init__(self,data,nNode):
        self.data = data
        self.nNode = nNode
    def __repr__(self):
        return "Node with value %d" % self.data

def printGrid(i):
    maxNum = i**2
    for j in range(maxNum):
        print("%3d"%(j+1),end="")
        if (j+1)%i==0:
            print()
        else:
            print("",end=" ")
