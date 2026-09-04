class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0

        while l < r:
            # Calculate current container area
            w = r - l
            h = min(height[l], height[r])
            current_area = w * h

            # Track maximum area seen so far
            max_water = max(max_water, current_area)

            # Move the pointer with the shorter height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water