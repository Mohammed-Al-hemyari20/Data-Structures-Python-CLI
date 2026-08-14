from .LinkedStack import LinkedStack
from ..model1.node import Node
from ..model1.models import readInt

def linked_stack_main():
    
    stack = LinkedStack()
    while True:
        print("\n====== Linked Stack Menu ========")
        print("1- Push")
        print("2- Pop")
        print("3- Peek")
        print("4- Display")
        print("5- git Size")
        print("6- Exit")
        print("================================")
        choice = input("Enter choice: ")

        match choice:
            case "1":
                val = readInt()
                stack.push(Node(val))
                print("Value pushed.")

            case "2":
                val = stack.pop()
                if val is not None:
                    print("Value Popped:", val)
                    
            case "3":
                top = stack.peek()
                if top is not None:
                    print("Top element:", top)
                    
            case "4":
                print("elements of Stack :")
                stack.display()
                
            case "5":
                val = stack.get_size()
                print("the size is: ", val)
            case "6":
                print("THE END...")
                break
            case _:
                print("Invalid choice Try again...")

