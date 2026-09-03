class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array

        for i, a in enumerate(nums):
            # Skip positive starting numbers (3 positive numbers can't sum to 0)
            if a > 0:
                break

            # Skip duplicate elements for the first position
            if i > 0 and a == nums[i - 1]:
                continue

            # Two Pointers setup
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicate elements for the second position
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res