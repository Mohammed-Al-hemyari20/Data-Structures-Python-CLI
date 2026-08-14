from ..model1.node import Node

class LinkedStack:
    def __init__(self):
        self.Top=None

    def push(self,item:Node):
        if self.Top==None:
            self.Top=item
            return
        item.Next=self.Top
        self.Top=item

    def display(self):
        if self.Top==None:
            print('list is empty')
            return
        temp=self.Top
        while temp!=None:
            print(temp.Data)
            temp=temp.Next

    def pop(self):
        if self.Top is None:
            print('list is empty')
            return None
        temp=self.Top
        self.Top=temp.Next
        temp.Next=None
        return temp.Data

    def peek(self):
        if self.Top is None:
            print('list is empty')
            return None
        return self.Top.Data

    def get_size(self):
        if self.Top is None:
            return 0
        counter=0
        temp=self.Top
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
       
#if __name__ == "__main__":

#example of specifying the main method
