class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def removeNode(root: Optional[TreeNode], target: int):
            if not root:
                return False

            if root.left and removeNode(root.left, target):
                root.left = None

            if root.right and removeNode(root.right, target):
                root.right = None

            # check AFTER processing children
            if not root.left and not root.right and root.val == target:
                return True

            return False

        result = removeNode(root, target)

        if result:
            return None

        return root