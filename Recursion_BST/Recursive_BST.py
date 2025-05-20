class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class recursive_bst():
    def __init__(self):
        self.root = None

    def recursive_contains(self,current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True 
        if value < current_node.value:
            return self.recursive_contains(current_node.left, value)
        if value > current_node.value:
            return self.recursive_contains(current_node.right, value)

    def r_contains(self, value):
        return self.recursive_contains(self.root, value)  
        




