class Stack:
    def __init__(self,size):
        self.Top=-1
        self.Data=[None] * size
        self.maxSize=size
        
    def isFull(self):
        return(self.Top == self.maxSize-1)
    def isEmpty(self):
        return(self.Top is -1)
    
    def push(self, item):
        """
          document ation commetns 
          @param item; the element to be pushed to the stack
        """
        if self.isFull():
            print('stack overflow')
            return
        self.Top+=1
        self.Data[self.Top]=item
        
    def pop(self):
        if self.isEmpty():
            print('stack underflow')
            return -1
        t=self.Data[self.Top]
        self.Top-=1
        return t
    
    def peek(self):
        if self.isEmpty():
            print('stack underflow')
            return -1
        t=self.Data[self.Top]
        return t
        
    def get_size(self):
        return self.Top+1
    
    def display(self):
        index=self.Top
        while(index>=0):
            print(self.Data[index])
            index-=1

    def transStack(self):
        if self.isEmpty():
            print('stack underflow')
            return None
        s1=Stack(self.get_size())
        while(not self.isEmpty()):
            s1.push(self.pop())
            
        #refill the original and new stack with all element
        s2=Stack(s1.get_size())
        while(not s1.isEmpty()):
            t=s1.pop()
            self.push(t)
            s2.push(t)
        return s2
    
 
