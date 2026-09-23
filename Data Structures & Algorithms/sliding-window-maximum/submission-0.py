from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = deque()  # Stores indices
        l = r = 0

        while r < len(nums):
            # Pop smaller values from the back of the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove left index if it is outside the current window
            if l > q[0]:
                q.popleft()

            # Append the maximum element to output once window reaches size k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
                
            r += 1

        return output