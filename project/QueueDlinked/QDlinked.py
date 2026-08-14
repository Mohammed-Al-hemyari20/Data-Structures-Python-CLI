from ..model1.DNode import Dnode

class QueueLinked_Double:
    def __init__(self):
        self.Front=None
        self.Rear=None
        
    def Enequeue(self, item):
        new_node = Dnode(item)
        '''
          describe your function work
        '''
        if self.Front==None:
            self.Front=self.Rear=new_node
            return
        self.Rear.Next=new_node
        new_node.Previous = self.Rear
        self.Rear=new_node
    def display(self):
        if self.Front==None:
            print('the queue is empty')
            return
        
        temp=self.Front
        while temp!=None:
            print(temp.data)
            temp=temp.Next

    def Dequeue(self):
        if self.Front is None:
            print('the Queue is empty')
            return
        
        temp=self.Front
        if temp.Next is None and temp.Previous is None:
            self.Front = None
            self.Rear = None
            return
        self.Front=self.Front.Next
        self.Front.Previous = None
        temp.Next=None
        return temp
    
    def get_size(self):
        if self.Front is None:
            return 0
        counter=0
        temp=self.Front
        while temp is not None:
            counter+=1
            temp=temp.Next
        return counter
    
    def get_length(self, mnode):
        #base condition: stop function loop
        if mnode is None:
            return 0
        #createria: coverge to base condition
        return 1 + self.get_length(mnode.Next)
    def getFront(self):
        if self.Front is None:
            return None
        return self.Front.data
    
    def getRear(self):
        if self.Rear is None:
            return None
        return self.Rear.data
