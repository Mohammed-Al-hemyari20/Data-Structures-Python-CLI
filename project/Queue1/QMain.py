from .Queue import Queue  

def queue_main():
    # size = int(input("Enter the size of the queue: "))
    q = Queue(10)
    
    while True:
        print("\n----Queue Menu----:")
        print("1- Enequeue")
        print("2- Dequeue")
        print("3- Get front ")
        print("4- Get Rear ")
        print("5- Queue Size")
        print("6- Delete Item")
        print("7- Display")
        print("8- Exit")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                item = int(input("Enter item to enqueue: "))
                q.Enequeue(item)
                
            case "2":
                val = q.dequeue()
                if val is not None:
                    print(f"Dequeued: {val}")
                
            case "3":
                front_item = q.get_front()
                if front_item is not None:
                    print(f"Front Item: {front_item}")
                    
            case "4":
                rear_item = q.get_rear()
                if rear_item is not None:
                    print(f"Rear Item: {rear_item}")
                    
            case "5":
                print(f"Queue size: {q.get_size()}")
                
            case "6":
                val = int(input("Enter item to delete: "))
                q.deletitem(val)
                
            case "7":
                q.display()
                
            case "8":
                print("Exiting ...")
                break
            case _:
                print("Invalid choice, Try again...")
                

