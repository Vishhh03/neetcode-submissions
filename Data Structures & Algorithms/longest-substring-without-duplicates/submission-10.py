class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                longest = max(longest, right-left+1)
                
            else:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
        return longest
