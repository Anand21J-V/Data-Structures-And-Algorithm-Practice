# CREATING A CLASS NODE FOR CONSTRUCTING THE NODE IN THE LINKED LIST
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# CREATING A DOUBLY LINKEDLIST CONSTRUCTOR
class DoublyLinkedlist():
    def __init__(self, value):
        New_node = Node(value)
        self.head = New_node
        self.tail = New_node
        self.length = 1


# METHOD TO CREATE A PRINTING FUNCTION
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# FUNCTION FOR ADDING A NEW NODE IN THE DOUBLY LINKED LIST
    def append(self, value):
        New_node = Node(value)
        if self.length == 0:
            self.head = New_node
            self.tail = New_node
        else:
            self.tail.next = New_node
            New_node.prev = self.tail
            self.tail = New_node    
        
        self.length += 1
        return True
    
# FUNCTION FOR DELETE THE LAST NODE FROM A DOUBLY LINKED LIST
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return True         


# FUNCTION FOR ADDING A NEW NODE IN THE BEGINNING OF THE DOUBLY LINKED LIST
    def prepend(self, value):
        New_node = Node(value)
        if self.length == 0:
            self.head = New_node
            self.tail = New_node
        else:
            New_node.next = self.head
            self.head.prev = New_node
            self.head = New_node
        self.length += 1
        return True         

# FUNCTION FOR DELETE THE FIRST NODE FROM A LINKED LIST
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value        

# FUNCTION TO GET ANY VALUE FROM THE DOUBLY LINKED LIST USING THE INDEX     
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length/2: 
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp        

# FUNCTION TO SET ANY VALUE AT THE DOUBLY LINKED LIST AT THE INDEX 
    def set_first(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
        self.length += 1
        return True

# FUNCTION TO INSERT ANY VALUE AT THE DOUBLY LINKED LIST AT ANY INDEX
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True 

# FUNCTION TO DELETE ANY VALUE AT THE LINKED LIST AT ANY INDEX 
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp.value
     


My_doubly_linkedlist = DoublyLinkedlist(4)
My_doubly_linkedlist.append(5)
My_doubly_linkedlist.append(6)
My_doubly_linkedlist.append(10)
My_doubly_linkedlist.append(12)
My_doubly_linkedlist.append(15)


print(My_doubly_linkedlist.remove(1))
print("New List")
My_doubly_linkedlist.print_list()