class Node:
    def __init__(self, value):
        self.value = value
        self.both = 0  # Initialize the XOR of next and previous pointers to 0

class XORLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.both = id(self.tail)  # XOR of the address of tail and 0
            self.tail.both ^= id(new_node)  # Update the XOR of previous tail's both field
            self.tail = new_node

    def get(self, index):
        current = self.head
        prev_id = 0  # Initially, the XOR of previous node and None is 0

        for i in range(index):
            if current is None:
                return None
            next_id = prev_id ^ current.both
            prev_id = id(current)
            current = dereference_pointer(next_id)

        return current

# Helper functions for pointer manipulation in Python (simulated)
def get_pointer(node):
    return id(node)

def dereference_pointer(ptr):
    return Node(ptr)

# Example :
xor_list = XORLinkedList()
xor_list.add(1)
xor_list.add(2)
xor_list.add(3)

node = xor_list.get(1)
if node:
    print(node.value)  
else:
    print("Node not found")
