from ..model1.DNode import Dnode
class Stack_linkedlist_Double:
    def __init__(self):
        self.Top = None
    
    def push(self, item):
        item= Dnode(item)
        if self.Top == None:
            self.Top = item
            return
        item.Next = self.Top
        self.Top.Previous = item
        self.Top = item
    def pop(self):
        if self.Top is None:
            print("the Stack is empty")
            return 
        data = self.Top.data
        temp = self.Top
        if temp.Next is None and temp.Previous is None:
            self.Top  = None
            return data
        self.Top = self.Top.Next
        self.Top.Previous = None
        temp.Next = None
        return data
    
    def peek(self):
        if self.Top is None:
            print("there is no Peek")
            return
        return self.Top.data
    
    def make_copy(self):
        if self.Top is None:
            return None
        
        s = Stack_linkedlist_Double()
        s2 = Stack_linkedlist_Double()
        while self.Top is not None:
            s.push(self.pop())  
        while s.Top is not None:
            val = s.pop()
            self.push(val)
            s2.push(val)
        return s2
            
        
        # while self.Top is not None:
        #     s.push(self.pop())
        # s2 = Stack_linkedlist_Double()
        # d = s.pop()
        # while d is not None:
        #     s2.push(d)
        #     self.push(d)
        #     d= s.pop()
        # return s2
        
    
    
    def display(self):
        if self.Top is None:
            print('list is empty')
            return
        temp=self.Top
        while temp!=None:
            print(temp.data)
            temp=temp.Next
            

    

        
