# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """ Brute force, O(n^2) """

        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]
        return maxProfit