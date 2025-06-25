class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self, value):
        New_node = Node(value)
        self.top = New_node
        self.height = 1


    def print_list(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        New_node = Node(value)
        if self.height == 0:
            self.top = New_node
        else:
            New_node.next = self.top
            self.top = New_node
        self.height += 1        

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None 
        self.height -= 1
        return temp.value         


My_Stack = Stack(4)

My_Stack.print_list()