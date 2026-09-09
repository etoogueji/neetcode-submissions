class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # stores pairs: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append((t, i))

        return res