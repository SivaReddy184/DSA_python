
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
                print(n.data)
                n =n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node


LL1 = LinkedList()
LL1.add_begin(10)
LL1.print_ll()
