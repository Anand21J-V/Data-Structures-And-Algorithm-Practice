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
    

    def min_value(self, current_node):
        while (current_node.left is not None):
            current_node = current_node.left
        return current_node.value 

    def __delete_node(self, current_node, value):
        if current_node == None: 
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value: 
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    
        

    def delete_node(self, value):
        self.__delete_node(self.root, value) 
        

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


