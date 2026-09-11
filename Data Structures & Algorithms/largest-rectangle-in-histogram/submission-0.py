class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []  # pairs: (start_index, height)

        for i, h in enumerate(heights):
            start = i
            # Pop bars that are taller than the current bar h
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index  # Move current bar's start index leftward
            stack.append((start, h))

        # Compute area for remaining bars that extend to the end
        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea