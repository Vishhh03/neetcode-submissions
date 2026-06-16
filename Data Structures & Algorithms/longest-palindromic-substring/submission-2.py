class Solution:
    def longestPalindrome(self, s: str) -> str:

        #FOR ODD PALINDROME
        #iterate over each index, for each index, if value of index-1 == index+1 (left,right),
        #   start while left and right from the index is same atleast once expand left and right'
        #       simultaneously, when loop fails store the string [left:right]

        #FOR EVEN PALINDROME
        #iterate over each index along with index+1 if index == index+1 and follow the same helper function
        #   to expand and check if value of left == right which will be index-1 == index+2
        
        #EXTRA
        #use helper function for expand and checking for value of left == right
        #iterate from [1] to [len-2] for ODD to prevent out of bounds 
        #while loop expand should check also for left < 0 or right > len-1

        def expand_check(left, right) -> str:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]      #not right - 1 since slicing will take care of that

        result = '' #(string,stringlength)
        result_len = 0
            #ODD PALINDROME CHECK
        for i in range(1,len(s)-1):
            palindrome = expand_check(i,i)
            if len(palindrome) > result_len:
                result = palindrome
                result_len = len(palindrome)

            #EVEN PALINDROME CHECK
        for i in range(1,len(s)-1):
            if s[i] == s[i+1]:
                palindrome = expand_check(i,i+1)
                if len(palindrome) > result_len:
                    result = palindrome
                    result_len = len(palindrome)

        return result