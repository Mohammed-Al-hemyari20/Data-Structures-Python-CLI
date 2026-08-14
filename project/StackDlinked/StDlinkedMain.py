from .StDlined import Stack_linkedlist_Double
from ..model1.DNode import Dnode
from ..model1.models import readInt, readFloat

def Dlinked_stack_main():
    
    stackDl = Stack_linkedlist_Double()
    while True:
        print("\n====== Linked Stack Menu ========")
        print("1- Push")
        print("2- Pop")
        print("3- Peek")
        print("4- Display")
        print("5- Make copy")
        print("6- Exit")
        print("================================")
        choice = input("Enter choice: ")

        match choice:
            case "1":
                val = readInt()
                stackDl.push(val)
                print("Value pushed.")

            case "2":
                val = stackDl.pop()
                if val is not None:
                    print("Value Popped:")
                    
            case "3":
                top = stackDl.peek()
                if top is not None:
                    print("Top element:", top)
                    
            case "4":
                print("elements of Stack :")
                stackDl.display()
                
            case "5":
                v = stackDl.make_copy()
                if v is not None:
                    v.display()
                else:
                    print("list is empty")
            case "6":
                print("THE END...")
                break
            case _:
                print("Invalid choice Try again...")

