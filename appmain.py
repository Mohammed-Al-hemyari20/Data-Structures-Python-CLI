from project.Array.Arraymain import ArrayMain
from project.linkedlist.linkedmain import LinkedListMain
from project.Dlinked.DlinkedMain import  DLinkedListMain
from project.Stack1.StackMain import stack_main
from project.Queue1.QMain import queue_main
from project.LinkedStack.StackMain import linked_stack_main
from project.LinkedQueue.QueueuMain import linked_queue_main
from project.StackDlinked.StDlinkedMain import Dlinked_stack_main
from project.QueueDlinked.QDlinkMain import Dlinked_queue_main

while True :
    print('===== Data Structure Menu=====')
    print('1- Array')
    print('2- Linked List')
    print('3- Doubly Linked List')
    print('4- Stack Arrays')
    print('5- Queue Arrays')
    print('6- Linked Stack')
    print('7- Linked Queue')
    print('8- Doubly Linked Stack')
    print('9- Doubly Linked Queue')
    print('10- Exit..')
    print('='*30)
    
    choice = input('What is your choice ? \n')
    match choice :
        case "1" :
            ArrayMain()
        case "2" :
            LinkedListMain()
        case "3" :
            DLinkedListMain()
        case "4" :
            stack_main()
        case "5" :
            queue_main()
        case "6" :
            linked_stack_main()
        case "7" :
            linked_queue_main()
        case "8" :
            Dlinked_stack_main()
        case "9" :
            Dlinked_queue_main()
        case "10" :
            print("THE END....")
            break
        case _ :
            print("Invalid, Try again")
            