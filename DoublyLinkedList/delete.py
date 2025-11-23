
class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linked list is empty yaar")
        else:
            n = self.head
            while n is not None:
                print(n.data,'---->', end=' ')
                n =n.nref

    def print_ll_reverse(self):
        print()
        if self.head is None:
            print("linked list is empty yaar")
        else:
            n = self.head
            while n.nref is not None:
                n =n.nref
            while n is not None:
                print(n.data, '---->', end=' ')
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("ll is not empty")

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n= self.head
            while n.nref is not None:
                n = n.nref
            new_node.pref = n
            n.nref = new_node


    def delete_begin(self):
        if self.head is None:
            print("dll is empty")
            return
        if self.head.nref is None:
            self.head = None
            print('dll is empty after deleting the node')
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("dll is empty")
            return
        if self.head.nref is None:
            self.head = None
            print('dll is empty after deleting the node')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("dll is empty")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
                print('dll is empty after deleting the node')
            else:
                print('node is not present in dll')
            return

        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            n = n.nref
        if n.nref is None:
            if n.data == x:
                n.pref.nref = None
                print('last node is deleted')
            else:
                print("no node in dll")
        elif n.pref is None:
            if n.data ==x:
                n.nref.pref = None
                self.head = n.nref
                print('first node is deleted')
        else:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
            print('middle node is deleted')



dl = DoublyLL()
dl.print_ll()
dl.insert_empty(10)
dl.add_begin(20)
dl.add_end(30)
dl.add_end(40)
dl.delete_by_value(20)
dl.print_ll()
dl.print_ll_reverse()

