# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        """ Hash table, O(n) """

        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap and abs(i - hashMap[nums[i]]) <= k:
                return True
            hashMap[nums[i]] = i
        return False

        """ Brute force, O(n^2) """

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False