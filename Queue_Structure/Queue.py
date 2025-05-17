class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self, value):
        New_node = Node(value)
        self.first = New_node
        self.last = New_node
        self.length = 1

    def print_list(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next    

    def enqueue(self, value):
        New_node = Node(value)
        if self.length == 0:
            self.first = New_node
            self.last = New_node
        else:
            self.last.next = New_node
            self.last = New_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None

        else:
            self.first = self.first.next
            temp.next = None

        self.length -= 1
        return temp.value    




My_Queue = Queue(5)

My_Queue.enqueue(4)
My_Queue.enqueue(5)
My_Queue.enqueue(6)
My_Queue.enqueue(7)

My_Queue.dequeue()
My_Queue.dequeue()
My_Queue.print_list()