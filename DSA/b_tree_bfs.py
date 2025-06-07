from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    total_sum = 0
    queue = deque([(root, root.val)])  # Queue stores (node, current_sum)

    while queue:
        node, cur_sum = queue.popleft()

        if not node.left and not node.right:
            total_sum += cur_sum
        
        if node.left:
            queue.append((node.left, cur_sum * 10 + node.left.val))
        if node.right:
            queue.append((node.right, cur_sum * 10 + node.right.val))

    return total_sum


root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(6)
root.right.right = TreeNode(7)

print(sumNumbers(root))

