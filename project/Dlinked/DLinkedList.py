from ..model1.DNode import Dnode

class DlinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None

    def isEmpty(self):
        return self.Head is None

    def addFirst(self, mNode):
        if self.isEmpty():
            self.Head = self.Tail = mNode
            return

        mNode.Next = self.Head
        self.Head.Previous = mNode
        self.Head = mNode

    def addLast(self, mNode):
        if self.isEmpty():
            self.Head = self.Tail = mNode
            return

        self.Tail.Next = mNode
        mNode.Previous = self.Tail
        self.Tail = mNode

    def addBefore(self, mNode, val):
        current = self.find(val)

        if current is None:
            print("Value not found.")
            return

        if current == self.Head:
            self.addFirst(mNode)
            return

        mNode.Next = current
        mNode.Previous = current.Previous
        current.Previous.Next = mNode
        current.Previous = mNode

    def addAfter(self, mNode, val):
        current = self.find(val)

        if current is None:
            print("Value not found.")
            return

        if current == self.Tail:
            self.addLast(mNode)
            return

        mNode.Next = current.Next
        mNode.Previous = current
        current.Next.Previous = mNode
        current.Next = mNode

    def addAt(self, data, pos):
        newnode = Dnode(data)

        if pos < 0:
            print("Invalid position")
            return

        if pos == 0:
            self.addFirst(newnode)
            return

        temp = self.Head
        i = 0

        while temp is not None and i < pos - 1:
            temp = temp.Next
            i += 1

        if temp is None:
            print("Position out of range")
            return

        if temp == self.Tail:
            self.addLast(newnode)
            return

        newnode.Next = temp.Next
        newnode.Previous = temp
        temp.Next.Previous = newnode
        temp.Next = newnode

    def deleteFirst(self):
        if self.isEmpty():
            print("List is empty.")
            return

        if self.Head == self.Tail:
            self.Head = self.Tail = None
            return

        self.Head = self.Head.Next
        self.Head.Previous = None

    def deleteLast(self):
        if self.isEmpty():
            print("List is empty.")
            return

        if self.Head == self.Tail:
            self.Head = self.Tail = None
            return

        self.Tail = self.Tail.Previous
        self.Tail.Next = None

    def deleteItem(self, val):
        node = self.find(val)

        if node is None:
            print("Value not found.")
            return

        if node == self.Head:
            self.deleteFirst()
            return

        if node == self.Tail:
            self.deleteLast()
            return

        node.Previous.Next = node.Next
        node.Next.Previous = node.Previous

    def deleteAt(self, pos):
        if pos < 0:
            print("Invalid position")
            return

        if pos == 0:
            self.deleteFirst()
            return

        temp = self.Head
        i = 0

        while temp is not None and i < pos:
            temp = temp.Next
            i += 1

        if temp is None:
            print("Position out of range")
            return

        if temp == self.Tail:
            self.deleteLast()
            return

        temp.Previous.Next = temp.Next
        temp.Next.Previous = temp.Previous

    def deleteAfter(self, val):
        current = self.find(val)

        if current is None or current.Next is None:
            print("Cannot delete.")
            return

        if current.Next == self.Tail:
            self.deleteLast()
            return

        temp = current.Next
        current.Next = temp.Next
        temp.Next.Previous = current

    def deleteBefore(self, val):
        current = self.find(val)

        if current is None or current.Previous is None:
            print("Cannot delete.")
            return

        if current.Previous == self.Head:
            self.deleteFirst()
            return

        temp = current.Previous
        temp.Previous.Next = current
        current.Previous = temp.Previous

    def find(self, val):
        curr = self.Head
        while curr:
            if str(curr.data) == str(val):
                return curr
            curr = curr.Next
        return None

    def display(self):
        curr = self.Head
        print("\nList Items:")
        while curr:
            print(curr.data, end=" <=> ")
            curr = curr.Next
        print("None\n")
        
    def display_recursive(self, mnode):
        if mnode is None:
            return
        #from begin to end
        print(mnode.data)
        self.display_recursive(mnode.Next)
        #from last to begin
        print(mnode.data)
        
    
    # def deleteAllitem(self, item):
    #     if self.isEmpty():
    #         return None
    #     val = self.find(item)
    #     while val is not None:
    #         self.deleteItem(item)
    #         val = self.find(item)
              
    # def d_tos(self):
    #     s = linked()
    #     if self.Head is None:
    #         return s
    #     temp = self.Head
    #     last = None
    #     while temp is:
    #         node = Node(temp.Data)
    #         if s.Head is None:
    #             s.Head = node
    #         else:
    #             last.Next = node
    #         last = node
    #         temp = temp.Next
    #     return s
                 