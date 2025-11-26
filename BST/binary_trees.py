class BST:
    def __init__(self, key):
        self.key = key
        self.l_child = None
        self.r_child = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return  # ignoring duplicates
        if self.key > data:
            if self.l_child:
                self.l_child.insert(data)  #recursive till leaf node to insert
            else:
                self.l_child = BST(data)
        else:
            if self.r_child:
                self.r_child.insert(data)
            else:
                self.r_child = BST(data)

    def search(self, data):
        if self.key == data:
            print('key is found at root')
            return
        if self.key > data:
            if self.l_child:
                self.l_child.search(data)
            else:
                print('Node is not present at left child sub tree')
        else:
            if self.r_child:
                self.r_child.search(data)
            else:
                print('Node is not present at right child sub tree')

    def preorder(self):
        if self.key is None:
            print('tree is empty')
            return
        print(self.key, end=' ')
        if self.l_child:
            self.l_child.preorder()
        if self.r_child:
            self.r_child.preorder()

    def inorder(self):
        if self.key is None:
            print('tree is empty')
            return
        if self.l_child:
            self.l_child.inorder()
        print(self.key, end=' ')
        if self.r_child:
            self.r_child.inorder()

    def postorder(self):
        if self.key is None:
            print('tree is empty')
            return
        if self.l_child:
            self.l_child.postorder()
        if self.r_child:
            self.r_child.postorder()
        print(self.key, end=' ')

    def delete(self, data,curr):
        """
        Delete a node with the given value (data) from the BST.

        Cases handled:
        1. Tree is empty → print message and return.
        2. Value lies in left subtree → recurse into left child.
        3. Value lies in right subtree → recurse into right child.
        4. Node found:
           a. Node has no left child → replace with right child.
           b. Node has no right child → replace with left child.
           c. Node has two children → replace with inorder successor
              (smallest value in right subtree), then delete successor.

        Returns:
            Node: The updated subtree root after deletion.
        """

        # Case 0: Empty tree
        if self.key is None:
            print("Tree is empty")
            return None

        # Case 1: Value is smaller → go left
        if data < self.key:
            if self.l_child:
                self.l_child = self.l_child.delete(data,curr)
            else:
                print("Given node is not present in left subtree")

        # Case 2: Value is larger → go right
        elif data > self.key:
            if self.r_child:
                self.r_child = self.r_child.delete(data,curr)
            else:
                print("Given node is not present in right subtree")

        # Case 3: Node found (data == self.key)
        else:
            # Subcase A: No left child → replace with right child
            if self.l_child is None:
                temp = self.r_child
                if data == curr:
                    self.key = temp.key
                    self.l_child = temp.l_child
                    self.r_child = temp.r_child
                    temp = None
                    return None
                return temp

            # Subcase B: No right child → replace with left child
            if self.r_child is None:
                temp = self.l_child
                # if root has to be deleted and root has only 1 right child
                if data == curr:
                    self.key = temp.key
                    self.l_child = temp.l_child
                    self.r_child = temp.r_child
                    return None
                return temp

            # Subcase C: Two children → find inorder successor
            node = self.r_child
            while node.l_child is not None:  # corrected condition
                node = node.l_child

            # Replace current key with successor's key
            self.key = node.key

            # Delete successor node from right subtree
            self.r_child = self.r_child.delete(node.key,curr)

        # Return current node (updated subtree root)
        return self

    def min_node(self):
        if self.l_child is None:
            print(self.key)
        else:
            self.l_child.min_node()
    def max_node(self):
        if self.r_child is None:
            print(self.key)
        else:
            self.r_child.max_node()

    def __str__(self):
        # Show key and children recursively
        #whenever we print an object this gets called, and this __str__ converts the object to readable str format
        #if we don't use this, then obj memory location will get printed
        return f'({self.key}, L={self.l_child.key if self.l_child else None}, R={self.r_child.key if self.r_child else None})'

def count(node):
    if node is None:
        return 0
    return 1 + count(node.l_child) + count(node.r_child)

root = BST(None)
root.insert(10)
list1 = [77,8,55,1, 2, 6,1234, 4,7,33]
for i in list1:
    root.insert(i)
root.min_node()
root.max_node()
root.search(4)
print('pre order')
root.preorder()
print()
print('in order')
root.inorder()
print()
print('post order')
root.postorder()
print()
if count(root) > 1:
    root.delete(88, root.key)
else:
    print('cant perform delete operation because only rot is present')
print('after deleting')
root.preorder()
print()
print(f'root {root.key}')
print(f'left child {root.l_child}')
print(f'right child {root.r_child}')
# print(f'right child"s left child {root.r_child.l_child}')
# print(f'right child"s right child {root.r_child.r_child}')
# print(f'left child"s left child {root.l_child.l_child}')
# print(f'right child"s left child {root.l_child.r_child}')
