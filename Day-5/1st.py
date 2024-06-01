class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
llist=LinkedList()
first_node=Node("Ashish")
llist.head=first_node
second_node=Node("Abhinay")
third_node=Node("suraj")
first_node.next=second_node
second_node.next=third_node

llist.print_list()