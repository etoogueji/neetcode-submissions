class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum must be in the right unsorted portion
                left = mid + 1
            else:
                # Minimum is mid or in the left portion
                right = mid

        # When left == right, we've converged on the minimum element
        return nums[left]