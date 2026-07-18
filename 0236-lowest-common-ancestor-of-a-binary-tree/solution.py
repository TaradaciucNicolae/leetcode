# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root == p or root == q: # adica daca root e exact ce cautam, il returnam
            return root
        

        # daca root nu e ce cautam noi, cautam in stanga si in dreapta

        left_node = self.lowestCommonAncestor(root.left ,p,q)
        right_node = self.lowestCommonAncestor(root.right ,p,q)

        # dupa ce s-a cautat in stanga si dreapta, practic va reitera si unul din el va gasi si unul nu va returna deci sigur va fi mai jos

        #daca amandoi au returan un nou, inseamna ca root e lca
        if left_node and right_node:
            return root

        else: # daca doar unul a returnat si unul inca cauta, si nu are rost,
              # automat cel commun ramane cel gasit
            return left_node or right_node
