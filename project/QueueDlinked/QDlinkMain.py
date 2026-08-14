from .QDlinked import QueueLinked_Double
from ..model1.DNode import Dnode
from ..model1.models import readInt, readFloat

def Dlinked_queue_main() :
    queueDl = QueueLinked_Double()
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
                queueDl.Enequeue(val)

            case "2":
                val = queueDl.Dequeue()
                print("value Dequeued:", val.data)

            case "3":
                queueDl.display()

            case "4":
                print("Front is: ", queueDl.getFront())

            case "5":
                print("Rear is: ", queueDl.getRear())

            case "6":
                print("Size is: ", queueDl.get_size())

            case "7":
                print("Exit")
                break
            case _:
                print("Invalid choice.")

