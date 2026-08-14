# from models import read, readFloat, readInt
from ..model1.node import Node

print('first line')
class LinkedQueue:
    def __init__(self):
        self.Front=None
        self.Rear=None

    def isEmpty(self):
        return (self.Front ==None) and (self.Rear==None)

    def Enequeue(self, item:Node):
        if self.isEmpty():
            self.Front=self.Rear=item
            return
        self.Rear.Next=item
        self.Rear=item

    def display(self):
        if self.Front==None:
            print('list is empty')
            return
        temp=self.Front
        while temp!=None:
            print(temp.Data)
            temp=temp.Next

    def Dequeue(self):
        if self.Front is None:
            print('list is empty')
            return None
        temp=self.Front
        self.Front=temp.Next
        temp.Next=None
        return temp.Data
    
    def getFront(self):
        if self.isEmpty():
            return None
        return self.Front.Data
    
    def getRear(self):
        if self.isEmpty():
            return None
        return self.Rear.Data
    
    def get_size(self):
        if self.Front is None:
            return 0
        counter=0
        temp=self.Front
        while temp is not None:
            counter+=1
            temp=temp.Next
        return counter
    
    def get_length(self,mnode):
        #base condition: the function call will end
        if mnode is None:
            return 0
        return 1+self.get_length(mnode.Next)
        # createria: function call itself and converge to base condition
