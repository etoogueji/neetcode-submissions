from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        # Min-heap storing tuples of (frequency, num)
        heap = []

        for num, cnt in count.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for cnt, num in heap]