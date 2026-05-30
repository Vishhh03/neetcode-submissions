class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maximum = 0
        seen = set()
        count = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                count -= 1
                continue    
            seen.add(s[right])
            count += 1
            maximum = max(count, maximum)
        return maximum
        