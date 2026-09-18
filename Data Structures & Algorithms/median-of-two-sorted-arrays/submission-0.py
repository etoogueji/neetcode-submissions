class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        # Ensure A is the smaller array to guarantee O(log(min(m, n)))
        if len(A) > len(B):
            A, B = B, A

        left, right = 0, len(A)

        while left <= right:
            i = (left + right) // 2  # Partition index in A
            j = half - i            # Partition index in B

            Aleft  = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i]     if i < len(A) else float("inf")
            Bleft  = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j]     if j < len(B) else float("inf")

            # Check if partition is valid
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements
                if total % 2 != 0:
                    return float(max(Aleft, Bleft))
                # Even total elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1