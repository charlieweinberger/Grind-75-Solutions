# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        
        """ Initial (inefficient) solution """

        numIterations = 0
        value = 0

        while value < x:
            numIterations += 1
            value += (2*numIterations + 1)

        return numIterations