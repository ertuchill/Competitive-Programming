#O(N) time complexity

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operatorset = {"+", "-", "/", "*"}
        stack=[]
        for t in tokens:
            if t in operatorset:
                second = stack.pop()
                first = stack.pop()
                if t=="+":
                    result = first + second
                    stack.append(result)
                if t=="-":
                    result = first - second
                    stack.append(result)
                if t=="/":
                    result = first / second
                    stack.append(int(result))
                if t=="*":
                    result = first * second
                    stack.append(result)
            else:
                stack.append(int(t))
        return stack[0]