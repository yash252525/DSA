class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self,data):
        # if data already exist , return (We do not use duplicates)
        if data == self.data:
            return

        if data < self.data:  # here we go to left subtree
            # value is less we add in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else: # here we switch to right subtree
            # value is less we add in right subtree
            
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements= []

        #visit left node (L)
        if self.left:
            elements+= self.left.in_order_traversal()
        
        # visit parent node (N)
        elements.append(self.data)

        # visit right node (R)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self,val):
        if val == self.data:
            return True
        
        if val < self.data:
            # it might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False



    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
            root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [17,4,1,20,9,23,18,34]
    number_tree = build_tree(numbers)
    print(number_tree.in_order_traversal())
    print(number_tree.search(20))
