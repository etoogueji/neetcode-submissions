class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair positions with speed and sort descending by position
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        stack = [] # Stores arrival times of distinct fleets

        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            
            # If current car takes <= time than the car ahead of it,
            # it catches up and merges into the ahead car's fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)