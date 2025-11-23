
#starting the linked list empty so ref and head is none
class Node:
    def __init__(self, data):
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
                print(n.data,'---->', end=' ')
                n =n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(100)
LL1.add_end(500)
LL1.add_begin(20)
LL1.print_ll()

#add at end with empty LL
LL2 = LinkedList()
LL2.add_begin(1000)
LL2.print_ll()