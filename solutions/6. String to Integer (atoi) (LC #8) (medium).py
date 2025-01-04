# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        
        # whitespace
        s = s.strip()

        # signedness

        if len(s) == 0:
            return 0

        sign = 1
        
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        # conversion

        stringIntegers = []
        for c in s:
            if c == "0" and len(stringIntegers) == 0:
                continue
            if c not in "0123456789":
                break
            stringIntegers.append(c)
        
        integer = 0
        maxInt = (2 ** 31)
        
        for i in range(len(stringIntegers)):
            
            exponent = len(stringIntegers) - i - 1
            tensPlace = (10 ** exponent)
            integer += (int(stringIntegers[i]) * tensPlace)
            
            # rounding
            if sign == 1 and integer > maxInt - 1:
                integer = maxInt - 1
                break
            if sign == -1 and integer > maxInt:
                integer = maxInt
                break
        
        # return
        return sign * integer