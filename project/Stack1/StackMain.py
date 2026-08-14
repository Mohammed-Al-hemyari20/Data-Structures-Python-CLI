from .Stack import Stack
def stack_main():
    S = Stack(7)
    
    while True:
        print("\n----- Stack Menu -----")
        print("1- Push")
        print("2- Pop")
        print("3- Peek")
        print("4- Display")
        print("5- git size")
        print("6- copy stack")
        print("7- Exit")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                item = int(input("Enter item to push: "))
                S.push(item)

            case "2":
                print("value Popped:", S.pop())

            case "3":
                print("Top element:", S.peek())

            case "4":
                print("Stack elements: ")
                S.display()
                
            case "5":
                print("The size of stack is : ",S.get_size())

            case "6":
                new = S.transStack()
                print("Copied stack is: ")
                new.display()
                
            case "7":    
                print("Exiting...")
                break
            case _:
                print("Invalid choice...")
                
