
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

    def after_node(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def before_node(self, data, x):
        if self.head is None:
            print("Linked list is empty sir")
            return

        #before the first node
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return

        n =  self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linked list not empty dude")

# exec for add begin and at the end of node
# LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.add_end(100)
# LL1.add_end(500)
# LL1.add_begin(20)
# LL1.print_ll()

# exec for add begin when ll is empty
# LL2 = LinkedList()
# LL2.add_begin(1000)
# LL2.print_ll()

#exec for after node
# LL3 = LinkedList()
# LL3.add_begin(100)
# LL3.add_end(300)
# LL3.after_node(200,500)
# LL3.print_ll()

# exec for before node
# LL4 = LinkedList()
# LL4.add_begin(10)
# LL4.before_node(20,10)
# LL4.before_node(30,0)
# LL4.print_ll()

# exec for insert empty
LL5 = LinkedList()
LL5.add_begin(20)
LL5.insert_empty(20)
LL5.print_ll()