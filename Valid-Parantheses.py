class Solution:
    def isValid(self, s: str) -> bool:
        if s == None or len(s) == 0 or len(s)%2!=0:
            return False
        stack = []
        for char in s:
            if char == '(': 
                stack.append(')')
                # print(stack)
            elif char == '[':
                stack.append(']')
                # print(stack)
            elif char == '{':
                stack.append('}')
                # print(stack)
            else:
                if len(stack) == 0 or char != stack.pop():
                    return False
            
        if len(stack)!=0:
            return False
        else:
            return True
            
                
