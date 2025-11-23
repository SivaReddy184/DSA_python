
#starting the linked list empty so ref and head is none
class Node:
    def __int__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linked list is empty yaar")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n =n.ref

LL1 = LinkedList()
LL1.print_ll()
