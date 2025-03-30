class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    if root is None:
        return
    
    queue = [root]  # Manual queue using a list
    
    while len(queue) > 0:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.pop(0)  # Pop first element (FIFO)
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Print level nodes manually without `join()`
        for i in range(len(level_nodes)):
            print(level_nodes[i], end=" ")
        print() 

# Example Usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

level_order_traversal(root)
