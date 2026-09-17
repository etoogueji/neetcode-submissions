from collections import defaultdict

class TimeMap:

    def __init__(self):
        # Maps key -> list of [value, timestamp]
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            t, v = values[mid]

            if t <= timestamp:
                res = v  # Candidate answer, try finding a closer timestamp to the right
                left = mid + 1
            else:
                right = mid - 1

        return res