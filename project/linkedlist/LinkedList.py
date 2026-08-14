from project.model1.node import Node
# class Node:
#     def __init__(self,data):
#         self.Next=None
#         self.Data=data

print('first line')
class LinkedList:
    def __init__(self):
        self.Head=None

    def addFirst(self,item:Node):
        if self.Head==None:
            self.Head=item
            return
        item.Next=self.Head
        self.Head=item

    def append(self, item:Node):
        if self.Head==None:
            self.Head=item
            return
        temp=self.Head
        while temp.Next!=None:
            temp=temp.Next
        temp.Next=item
        #print ("addition success")

    def Addat_position(self, position, new_value):
        if position <= 0:
            print("Invalid position")
            return
        newnode = Node(new_value)
        if position == 1:
            self.addFirst(newnode)
            return
            
        temp = self.Head
        i = 1
        while i < position -1 and temp is not None:
            temp = temp.Next
            i += 1
        if temp is None:
            print("position is not found")
            return
        newnode.Next = temp.Next
        temp.Next = newnode

    def Addafter_value(self, value, new_value):
        temp = self.Head
        while temp is not None:
            if temp.Data == value:
                newnode = Node(new_value)
                newnode.Next = temp.Next
                temp.Next = newnode
                return
            temp = temp.Next
        print("the value is not found ")
        
    def display(self):
        if self.Head==None:
            print('list is empty')
            return
        temp=self.Head
        while temp!=None:
            print(temp.Data, end=" -> ")
            temp=temp.Next
        print("None")

    def deleteFirst(self):
        if self.Head is None:
            print('list is empty')
            return
        temp=self.Head
        self.Head=temp.Next
        temp.Next=None
    
    def deleteLast(self):
        if self.Head is None:
            print('the list is empty')
            return
        if(self.Head.Next is None):# the has only one node
            self.Head=None
            return
        temp=self.Head
        while temp.Next.Next is not None:
            temp=temp.Next
        temp.Next = None
            
        # delete with value
    def deleteItem(self, value):
        if self.Head is None:
            print("list is empty")
            return
        
        if self.Head.Data == value:
            temp = self.Head
            self.Head = temp.Next
            temp.Next = None
            return
            
        temp = self.Head
        while temp.Next is not None:
            if temp.Next.Data == value:
                dell = temp.Next
                temp.Next = dell.Next
                dell.Next = None
                return
            temp = temp.Next
        print("the value is not found")
        
        
    #  delete with position
    def delete_withposition(self, position):
        size = self.get_size()
        if position < 1 or position > size:
            print('Position out of bounds')
            return
        if self.Head is None:
            print('list is empty')
            return
        if position == 1:
            self.deleteFirst()
            return
        temp = self.Head
        counter = 1
        while temp is not None and counter < position -1:
            temp = temp.Next
            counter += 1
        if temp is None:
            print('Position out of bounds')
            return
        temp.Next = temp.Next.Next
        
    def get_size(self):
        if self.Head is None:
            return 0
        counter=0
        temp=self.Head
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

    def find(self, item):
        if self.Head is None:
             return None
        temp=self.Head
        while temp is not None:
            if temp.Data==item:
                break
            temp=temp.Next
        return temp
    
    def findAt(self, position):
        if self.Head is None:
             return None
        size = self.get_size()
        if position < 1 or position > size: 
            print('position not exist Size = ', size)
            return None
        
        counter = 1 
        temp = self.Head
        while temp is not None:
            if position == counter:
                break
            counter += 1
            temp = temp.Next

        return temp
    
    def deleteAll(self):
        # to delete all nodes
        if self.Head is None:
            return None
        s = self.get_size()
        for i in range(s):
            self.deleteFirst()
    
    # طريقة اخرى لحذف كل النودات
    # def deleteAll(self):
    #     if self.Head is None:
    #         return None
    #     temp = self.Head
    #     while temp is not None:
            # curr = temp.Next
            # temp.Next = None
            # temp = curr
    #     self.Head = None
    
    
    def linked_toArray(self):
        # linked to array
        if self.Head is None:
            return None
        arr = []
        temp = self.Head
        while temp is not None:
            arr.append(temp.Data)
            temp = temp.Next
        arr.reverse()
        print(arr)
    