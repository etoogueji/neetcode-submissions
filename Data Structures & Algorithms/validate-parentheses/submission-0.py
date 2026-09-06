class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        validCombo = {")": "(", "]":"[", "}": "{"}

        for char in s:
            if char in validCombo:
                if stack and stack[-1] == validCombo[char]:
                    stack.pop()
                else: return False
            else:
                stack.append(char)

        return True if not stack else False


        