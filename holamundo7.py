class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_unival_subtrees(root):
    def is_unival(node, value):
        if node is None:
            return True
        if node.value != value:
            return False
        return is_unival(node.left, value) and is_unival(node.right, value)

    def helper(node):
        if node is None:
            return 0, True

        left_count, is_left_unival = helper(node.left)
        right_count, is_right_unival = helper(node.right)

        if is_left_unival and is_right_unival and (node.left is None or node.value == node.left.value) and (node.right is None or node.value == node.right.value):
            return left_count + right_count + 1, True
        else:
            return left_count + right_count, False

    count, _ = helper(root)
    return count

# Example usage:
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(0)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(1)

print(count_unival_subtrees(root))  
