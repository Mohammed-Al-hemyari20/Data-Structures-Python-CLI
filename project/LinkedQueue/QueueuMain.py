from ..model1.node import Node
from .LinkedQueue import LinkedQueue
from ..model1.models import readInt, readFloat

def linked_queue_main() :
    queue = LinkedQueue()
    while True:
        print("\n--- Linked Queue Menu ---")
        print("1- Enqueue")
        print("2- Dequeue")
        print("3- Display")
        print("4- Get Front")
        print("5- Get Rear")
        print("6- Get Size")
        print("7- Exit")

        choice = input('Enter your choice: ')

        match choice:
            case "1":
                val = readInt()
                queue.Enequeue(Node(val))
            
            case "2":
                val = queue.Dequeue()
                print("value Dequeued:", val)

            case "3":
                queue.display()

            case "4":
                print("Front is: ", queue.getFront())

            case "5":
                print("Rear is: ", queue.getRear())

            case "6":
                print("Size is: ", queue.get_size())

            case "7":
                print("Exit")
                break
            case _:
                print("Invalid choice.")

