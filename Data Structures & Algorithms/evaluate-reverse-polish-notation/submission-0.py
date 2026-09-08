class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))  # Truncates toward zero
            else:
                stack.append(int(c))

        return stack[0]