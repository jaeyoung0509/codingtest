
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root : 
            return False
        if self.isSametree(root , subRoot):
            return True
        return  self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot) 
    def isSametree(self , r : Optional[TreeNode] , s : Optional[TreeNode]):
        if r and s  :
            return r.val == s.val and self.isSametree(r.left , s.left) and  self.isSametree(r.right , s.right) 
        
        return False