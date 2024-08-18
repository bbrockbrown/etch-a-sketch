class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def searchBST(root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if root is None:
        return root
    
    if root.val == val:
        return root
    elif root.val < val:
        root = root.right
    elif root.val > val:
        root = root.left
    
    searchBST(root, val)
    
print(searchBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))))