
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

    def add_after(self, data, x):
        if self.head is None:
            print('ll is empty dude')
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print('given node is not there in dll')
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print('ll is empty dude')
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print('given node is not there in dll')
            else:
                new_node = Node(data)
                new_node.pref = n.pref
                new_node.nref = n
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node







dl = DoublyLL()
dl.print_ll()
dl.insert_empty(10)
#dl.add_begin(20)
dl.add_end(100)
dl.add_end(200)
dl.add_begin(1000)
dl.add_after(300,200)
dl.add_before(20,100)
dl.print_ll()
dl.print_ll_reverse()

