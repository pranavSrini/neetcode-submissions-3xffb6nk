from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        if(len(s) % 2 != 0): return False
        for c in s:
            if(c == '[' or c == "(" or c == "{"):
                stack.append(c)
            else:
                if(len(stack) == 0): return False

                top = stack.pop()
                if(top == '[' and c != ']'):
                    return False
                if(top == '(' and c != ')'):
                    return False
                if(top == '{' and c != '}'):
                    return False

        if(len(stack) != 0): return False
                    
        
        #Later brackets must be closed first, Hence LIFO


        
        return True




        