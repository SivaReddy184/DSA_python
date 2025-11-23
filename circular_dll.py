class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None

class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def printc(self):
        if self.head is None:
            print('circular dll is empty')
        else:
            n = self.head
            while True:
                print(n.data,'------', end=' ')
                n = n.nref
                if n == self.head:
                    break

    def printc_reverse(self):
        print()
        if self.tail is None:
            print('cdll is empty')
        else:
            n = self.tail
            while True:
                print(n.data, '-----', end=' ')
                n = n.pref
                if n == self.tail:
                    break

    def add_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            new_node.nref = new_node
            new_node.pref = new_node
        else:
            print("cdll is not empty")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.nref = new_node
            new_node.pref = new_node
        else:
            new_node.nref = self.head
            new_node.pref = self.tail
            self.head.pref = new_node
            self.tail.nref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.pref = self.tail
            new_node.nref = self.head
            self.tail.nref = new_node
            self.head.pref = new_node
            self.tail =  new_node

    def add_by_value(self,x):
        pass

    def delete_begin(self):
        pass

    def delete_end(self):
        pass

    def delete_by_value(self,x):
        pass


cl = CircularDLL()
cl.add_empty(10)
cl.add_begin(20)
cl.add_begin(30)
cl.add_end(40)
cl.printc()
cl.printc_reverse()
