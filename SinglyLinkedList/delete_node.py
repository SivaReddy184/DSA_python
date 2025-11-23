
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

    def delete_begin(self):
        if self.head is None:
            print("ll is empty")
        else:
            self.head = self.head.ref
            #making the next element head so that 1st ones delete

    def delete_end(self):
        if self.head is None:
            print("ll is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("ll is empty")
            return
        # if given node is 1st node
        if self.head.data == x:
            self.head = self.head.ref #changing first node ref to 2nd to delete 1st node

        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print('Node not found in ll')
        else:
            n.ref = n.ref.ref





# # delete begin exec
# LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(20)
# #LL1.print_ll()
# LL1.delete_begin()
# LL1.print_ll()

# # delete end exec
# LL1 = LinkedList()
# LL1.add_begin(10)
# #LL1.add_begin(20)
# #LL1.print_ll()
# LL1.delete_end()
# LL1.print_ll()

# delete nodeby value
LL2 = LinkedList()
LL2.add_begin(10)
LL2.add_end(30)
LL2.print_ll()
LL2.delete_by_value(30)
LL2.print_ll()