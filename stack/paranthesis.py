class Solution:
    def isValid(self, s: str) -> bool:
        frontset = {'(','[','{'}
        rearset = {')',']','}'}
        stack = []
        for c in s:
            print(c)
            if c in frontset:
                stack.append(c)
            if c in rearset:
                if len(stack) == 0:
                    return False
                match = stack.pop()
                if match == '(':
                    if c != ')':
                        return False
                elif match == '[':
                    if c != ']':
                        return False
                elif match == '{':
                    if c != '}':
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False