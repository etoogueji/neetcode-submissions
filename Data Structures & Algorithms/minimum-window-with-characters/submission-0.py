class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        window = {}
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # Check if current character satisfies required count in t
            if c in countT and window[c] == countT[c]:
                have += 1

            # Try to shrink window from left while condition is met
            while have == need:
                # Update our minimum window result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""