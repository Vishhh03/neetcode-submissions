

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}    # Key -> Frequency Array ; Value -> anagram string List
        for string in strs:
            freq = [0] * 26 # Frequency Array for chars
            for char in string:
                freq[ord(char) - ord('a')] += 1     # Find index with ord() that gets the Unicode value
            if tuple(freq) not in group:
                group[tuple(freq)] = []    
            group[tuple(freq)].append(string)
        return list(group.values()) 
