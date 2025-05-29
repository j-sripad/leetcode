# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
        
            if root is None:
                return 
            
            current_value = root.val
            left_value = dfs(root.left) #list of list
            right_value = dfs(root.right)
            
            if left_value and right_value:
                for l in left_value:
                    l.append(current_value)
                for r in right_value:
                    r.append(current_value)
                
                return left_value + right_value
            elif left_value and not right_value:
                for l in left_value:
                    l.append(current_value)
                return left_value
            elif right_value and not left_value:
                for r in right_value:
                    r.append(current_value)
                return right_value
            else:
                return [[current_value]]

        output = dfs(root)
        total = 0
        for out in output:
            total+=int(''.join(map(str,out[::-1])))
        return total

            
            


        