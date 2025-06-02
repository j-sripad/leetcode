class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # print(path.split('/'))
        for p in path.split('/'):
            if p == '/' or p=='.' or p=='':
                continue
            elif p == '..':
                if len(stack)>0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(p)

        return  '/'+ '/'.join(stack)
            





