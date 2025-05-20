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


    def recursive_contains(self,current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True 
        if value < current_node.value:
            return self.recursive_contains(current_node.left, value)
        if value > current_node.value:
            return self.recursive_contains(current_node.right, value)
        
    def recursive_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.recursive_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.recursive_insert(current_node.right, value)
        return current_node.value        

    def r_contains(self, value): 
        return self.recursive_insert(self.root, value)  
        

My_tree = Binary_search_tree()
My_tree.insert(2)
My_tree.insert(1)
My_tree.insert(3)
My_tree.insert(12)
My_tree.insert(10)
My_tree.insert(6)
My_tree.insert(13)
My_tree.insert(15)


print(My_tree.r_contains(20))


