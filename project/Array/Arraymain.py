from .Arrays import ArrayClass

def ArrayMain():
    # s = int(input("Enter the size of Array"))
    array = ArrayClass(10)
    while True:
        print("\n----- Array Menu -----")
        print("1- Add Element")
        print("2- Delete Element")
        print("3- Delete All Element that repetition")
        print("4- Delete without the first repetition")
        print("5- Delete without the second repetition")
        print("6- Delete without the third repetition")
        print("7- Delete without the last repetition")
        print("8- Print Array")
        print("9- array to list")
        print("10- To print list")
        print("11- Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                array.insert()
                
            case "2":
                f = int(input("Enter value to delete: "))
                array.removeItem(f)
                
            case "3":
                d = int(input("Enter value to delete: "))
                array.removeAllItems_theSame(d)

            case "4":
                d = int(input("Enter value to delete: "))
                array.removeAll_without1(d)
                
            case "5":
                d = int(input("Enter value to delete: "))
                array.removeAll_without2(d)
                
            case "6":
                d = int(input("Enter value to delete: "))
                array.removeAll_without3(d)
                
            case "7":
                d = int(input("Enter value to delete: "))
                array.removeAll_withoutlast(d)
                
            case "8":
                array.display()
                
            case "9":
                res = array.arr_tolinked()
                print ("Ok, this is the Head => ", res.Data)

            case "10":
                array.display1(res)    
                
            case "11":
                print("Exiting program...")
                break

            case _:
                print("Invalid choice, try again.")

