class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root is None:
        return "None"  # Serialize None as a string
    left = serialize(root.left)
    right = serialize(root.right)
    return f"{root.val},{left},{right}"

def deserialize(s):
    def helper(nodes):
        val = next(nodes)
        if val == "None":
            return None
        node = Node(int(val))
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node

    values = s.split(',')
    nodes = iter(values)
    return helper(nodes)

# Example usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

# Serialize the tree to a string
serialized_tree = serialize(root)
print(serialized_tree)  

# Deserialize the string back into a tree
deserialized_tree = deserialize(serialized_tree)
