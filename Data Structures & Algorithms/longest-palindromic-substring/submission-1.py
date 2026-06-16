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

        def expand_check(left, right) -> int:
            count = 0
            while left-(count+1) >= 0 and right+(count+1) < len(s) and s[left-(count+1)] == s[right+(count+1)]:
                count += 1
            return count

        result = '' #(string,stringlength)
        result_len = 0
            #ODD PALINDROME CHECK
        for i in range(1,len(s)-1):
            count = expand_check(i,i)
            if count > 0:
                if count*2 + 1 > result_len:
                    result = s[i-count:i+count+1]

            #EVEN PALINDROME CHECK
        for i in range(1,len(s)-1):
            if s[i] == s[i+1]:
                count = expand_check(i,i+1)
                if count > 0:
                    if count*2 + 1 > result_len:
                        result = s[i-count:i+count+1]
                else:
                    return s[i:i+2]
        if result == '':
            return s[0] 
        else:
            return result