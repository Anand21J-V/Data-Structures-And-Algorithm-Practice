class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_search_tree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        New_node = Node(value)

        if self.root is None:
            self.root = New_node
            return True
        
        temp = self.root
        while (True):
            if New_node.value == temp.value:
                return False
            if New_node.value < temp.value:
                if temp.left is None:
                    temp.left = New_node
                    return True
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = New_node
                    return True
                temp = temp.right      

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left            
            elif value > temp.value:
                temp = temp.right
            else:
                return True    

        return False



My_tree = Binary_search_tree()
My_tree.insert(2)
My_tree.insert(1)
My_tree.insert(3)
My_tree.contains(1)


print(My_tree.contains(1))


