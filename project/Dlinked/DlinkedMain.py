from .DLinkedList import DlinkedList
from ..model1.DNode import Dnode
from ..model1.models import readInt

def DLinkedListMain():
    d_list = DlinkedList()

    while True:
        print("\n----- Doubly Linked List Menu -----")
        print("1- Add First")
        print("2- Add Last")
        print("3- Add Before")
        print("4- Add After")
        print("5- Add At Position")
        print("6- Delete First")
        print("7- Delete Last")
        print("8- Delete Item")
        print("9- Delete At Position")
        print("10- Delete Before")
        print("11- Delete After")
        print("12- Find")
        print("13- Display")
        print("14- displayRecursive")
        print("15- Exit")

        choice = input("Choice: ")

        match choice:
            case "1":
                d_list.addFirst(Dnode(readInt()))

            case "2":
                d_list.addLast(Dnode(readInt()))

            case "3":
                data = readInt()
                val = input("Before which value? ")
                d_list.addBefore(Dnode(data), val)

            case "4":
                data = readInt()
                val = input("After which value? ")
                d_list.addAfter(Dnode(data), val)

            case "5":
                data = readInt()
                pos = readInt()
                d_list.addAt(data, pos)

            case "6":
                d_list.deleteFirst()

            case "7":
                d_list.deleteLast()

            case "8":
                val = input("Value to delete: ")
                d_list.deleteItem(val)

            case "9":
                pos = readInt()
                d_list.deleteAt(pos)

            case "10":
                val = input("Delete before value: ")
                d_list.deleteBefore(val)

            case "11":
                val = input("Delete after value: ")
                d_list.deleteAfter(val)

            case "12":
                val = input("Find: ")
                node = d_list.find(val)
                print("Found:", node.data if node else "Not found")

            case "13":
                d_list.display()
                
            case "14":
                if d_list.Head is None:
                    print("list is empty")
                else:
                    mnode = d_list.Head
                    d_list.display_recursive(mnode)
                
            case "15":
                print("Exit>...")
                break
            case _:
                print("Invalid, Try again")
    