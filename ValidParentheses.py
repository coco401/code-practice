class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        mapping = {'[':']', 
                   '{':'}',
                   '(':')'}
        stack = []
        
        for i in s:
            if i in mapping:
                stack.append(i)
            elif (not stack) or (i != mapping[stack.pop()]):
                return False
            
        return len(stack) == 0