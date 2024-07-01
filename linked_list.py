class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    #append new node
    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    #print ll
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  

    #prepend new node
    def prepend(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    #delete node by value
    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        
        prev_node.next = current_node.next
        current_node = None


# Create a linked list and append some elements
llist = linked_list()
llist.append("A")
llist.append("B")
llist.append("C")

# Print the linked list
llist.print_list()  # Output: A -> B -> C -> None

# Prepend an element
llist.prepend("D")
llist.print_list()  # Output: D -> A -> B -> C -> None

# Delete an element
llist.delete_node("B")
llist.print_list()  # Output: D -> A -> C -> None
