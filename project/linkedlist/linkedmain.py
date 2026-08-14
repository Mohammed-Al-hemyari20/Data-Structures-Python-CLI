from.LinkedList import LinkedList
from project.model1.node import Node
from project.model1.models import readInt, read, readFloat

def LinkedListMain():
    L_list = LinkedList()

    while True:
        print("\n----- S Linked List Menu -----")
        print("1- Add First")
        print("2- Append (Add Last)")
        print("3- Add After value")
        print("4- Add At Position")
        print("5- Delete First")
        print("6- Delete Last")
        print("7- Delete Item")
        print("8- Delete At Position")
        print("9- Delete all nodes")
        print("10- git size")
        print("11- git length")
        print("12- Find Item")
        print("13- Find At position")
        print("14- Display")
        print("15- linked to Array")
        print("16- Exit")

        choice = input(" Enter your Choice: ")

        match choice:
            case "1":
                L_list.addFirst(Node(readInt()))

            case "2":
                L_list.append(Node(readInt()))

            # case "3":
            #     data = readInt()
            #     val = input("Before which value? ")
            #     L_list.addBefore(Node(data), val)

            case "3":
                data = readInt()
                val = input("After which value? ")
                L_list.Addafter_value(val, data)

            case "4":
                data = readInt()
                pos = int(input("enter the pos"))
                L_list.Addat_position(pos, data)

            case "5":
                L_list.deleteFirst()

            case "6":
                L_list.deleteLast()

            case "7":
                val = input("Value to delete: ")
                L_list.deleteItem(val)

            case "8":
                pos = int(input("enter pos to delete"))
                L_list.delete_withposition(pos)
            
            case "9":
                L_list.deleteAll()

            case "10":
                size = L_list.get_size()
                print(f"size of linked list: {size}")

            case "11":
                mnode = L_list.Head
                res = L_list.get_length(mnode)
                print("The length: ", res)

            case "12":
                val = readInt()
                node = L_list.find(val)
                if node is not None:
                    print("found", node.Data)
                    return
                print("Not found ")
                
            case "13":
                pos = int(input("Enter position: "))
                node = L_list.findAt(pos)
                if node:
                    print("Node at position", pos, "is:", node)
                    return
                print("Not found ")
                
            case "14":
                L_list.display()
                
            case "15":
                L_list.linked_toArray()
                
            case "16":
                print("THE END...")
                break
                
            case _:
                print("Try again")


