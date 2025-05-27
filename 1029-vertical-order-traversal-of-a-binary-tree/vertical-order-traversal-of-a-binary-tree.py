# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        origin = (0,0)
        coordinates = []
        node_values = {} # here key is column value

        

        def dfs(root,point):
            if not root:
                return
            else:
                
                
                coordinates.append([point[0],point[1],root.val])
            dfs(root.left, (point[0]+1, point[1]-1))
            dfs(root.right, (point[0]+1, point[1]+1))

        dfs(root, origin)

        coordinates.sort()
        node_values = {}
        for r,c,v in coordinates:
            if c in node_values:
                node_values[c].append(v)
            else:
                node_values[c] = [v]


        node_values = dict(sorted(node_values.items()))


        
        return list(node_values.values())

