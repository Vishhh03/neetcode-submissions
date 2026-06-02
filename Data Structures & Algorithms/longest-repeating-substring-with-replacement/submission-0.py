from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maximum = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1 
            maximum = max(maximum, count[s[r]])
            if (r-l+1) - maximum <= k: 
                continue
            else:
                count[s[l]] -= 1
                l += 1
        return r-l+1