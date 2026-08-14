from project.model1.node import Node

class ArrayClass:
 
    
    def __init__(self,size):
        self.size=size
        self.data=[]

    def insert(self):
        print('Enter Array Elements: \n')
        for i in range(self.size):
            self.data.append(int(input('Enter value')))

    def display(self):
        print('the element of Array are :')
        print(self.data)
        # for i in range(self.size):
        #     print(self.data[i])
    
    def removeItem(self,item):
        self.data.remove(item)
        self.size=self.size-1

     
    def removeAllItems_theSame(self, item):
        # function to delete all items that were repeated than once(this item which user enter it)
        total_iteration=self.data.count(item)
        for i in range(total_iteration):
            self.data.remove(item)
        self.size=self.size-total_iteration
        
    
    def removeAll_without1(self, item):
        # function to delete all items that were repeated than once without the first(this item which user enter it)
        for i in range(self.size):
            if self.data[i] == item: 
                self.removeAllItems_theSame(item)
                self.data.insert(i,item)
                self.size +=1 
                return
        print("not found")
    
    # ======================
    def removeAll_without2(self, item):
        # the same but without the secound repetition
        if self.data[0] == item:
            self.removeItem(item)
        for i in range(self.size):
            if self.data[i] == item:
                self.removeAllItems_theSame(item)
                self.data.insert(i,item)
                self.size +=1
                return
        print("not found")
    #  ============================
      
    def removeAll_without3(self, item):
        # the same but without the third repetition
        c = 0
        i = 0
        while i < len(self.data):
            if self.data[i] == item:
                c +=1
                if c != 3:
                    self.data.pop(i)
                    self.size -=1
                    continue
            i +=1
        
    def removeAll_withoutlast(self, item):
        # the same but without the last repetition
        self.data.reverse()
        for i in range(self.size):
            if self.data[i] == item: 
                self.removeAllItems_theSame(item)
                self.data.insert(i,item)
                self.size +=1 
                self.data.reverse()
                return
        print("not found")
    
    def deleteall(self):
        # delete all items from the array
        for i in range(self.size):
            self.data.pop()
    
    # array to list
    def arr_tolinked(self):
        if self.size == -1:
            print("list is empty")
            return
        
        Head = Node(self.data[0])
        temp = Head
        for i in range(1, self.size):
            temp.Next = Node(self.data[i])
            temp = temp.Next
        return Head
            
    def display1(self, Head):
        temp=Head
        while temp!=None:
            print(temp.Data, end=" => " )
            temp=temp.Next
        print("none")
        