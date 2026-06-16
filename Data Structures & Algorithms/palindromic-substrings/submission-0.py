class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        #helper expand function
        def expand(left,right) -> int:
            count = 0
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                count += 1
                left -= 1
                right += 1
            return count

        #ODD check
        for i in range(len(s)):
            result += expand(i,i)

        for i in range(len(s)-1):
            result += expand(i,i+1) 
        
        return result