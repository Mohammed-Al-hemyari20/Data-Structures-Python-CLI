class Queue:  # procces in momery and the stack cpu scheduling
    def __init__(self,size):
        self.front = -1
        self.rear = -1
        self.data = [0]*size
        self.MaxSize = size
        
    def is_Empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return self.rear == self.MaxSize -1
    
    def reset(self):
        self.front =self.rear=-1
        
    def Enequeue(self,item):
        if self.is_full() and self.is_Empty():
            self.reset()
            self.rear+=1
            self.data[self.rear]= item
            return
        if self.is_full():
            print("The queue is full")
            return
        self.rear+=1
        self.data[self.rear]= item
        if self.front == -1:
            self.front = 0
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_Empty():
            if self.is_Empty() and self.is_full():
                self.reset()
                print("try another time")
                return
            else:
                print("The Queue is empty")
                return
        
        res = self.data[self.front]
        self.front+=1
        return res
    
    def get_front(self):
        if self.is_Empty():
            print("try anotehr time")
            return
        return self.data[self.front]
                            
    def get_rear(self):
        if self.is_Empty():
            print("try anotehr time")
            return
        return self.data[self.rear]
    
    def deletitem(self,item):
        if self.is_Empty():
            print("the queue is empty")
            return
        
        start = self.front+1
        found = False
        while (start<=self.rear):
            if self.data[start]==item:
                found = True
                index = start
                while index<self.rear:
                    self.data[index] = self.data[index+1]
                    index+=1
                self.rear-=1
                break
                
            start+=1
        if not found:
            print("not found")
            # if found is True:
                # break
            
    def get_size(self):
        if self.is_Empty():
            return 0
        return self.rear - self.front + 1
            
    def display(self):
        if self.is_Empty():
            print("the queue is empty")
            return
        index = self.front
        while index <= self.rear:
            print(self.data[index])
            index+=1
            