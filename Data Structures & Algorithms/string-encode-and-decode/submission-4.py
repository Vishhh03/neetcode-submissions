class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for word in strs:
            output += str(len(word))+'#'+word
        print (output)
        return output
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):             # till i=16
#       12#twelveletter6#      i=0
#       01234567890123456      j=0
            j = i+1
            while s[j] != '#':
                j += 1
            if s[j] == '#':                  #                           j=1
                num = int(s[i:j])    #   str(s[0:2]) ->  num=12
                result.append(s[j+1:j+1+num])  # [3:15]
                i = j+1+num
        return result

