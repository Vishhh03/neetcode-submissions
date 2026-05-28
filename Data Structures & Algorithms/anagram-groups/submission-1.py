from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            charCount = [0] * 26
            for char in word:
                charCount[ord(char) - ord('a')] += 1

            charCount = tuple(charCount)

            if charCount not in map:
                map[charCount] = []
            map[charCount].append(word)
        return list(map.values())