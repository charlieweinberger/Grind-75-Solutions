# https://leetcode.com/problems/3sum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """ sorting + two pointers """

        # sort the input list, so that it's in increasing order.
        nums.sort()
        
        n = len(nums)
        triplets = []

        # repeatedly use two-pointers method, starting at different points.
        for start in range(len(nums)):

            # if current start is the same as previous start, the triplets
            # will be the same, so we just continue to the next start here
            if start > 0 and nums[start] == nums[start - 1]:
                continue

            # classical two pointers here, starting just after 'start' and
            # ending at the last index of the list.
            left = start + 1
            right = n - 1

            while left < right:

                total = nums[left] + nums[right] + nums[start]

                # if the current total is less than zero, then we increase
                # our left pointer, which means the value at left will be
                # greater. The opposite applies for out right pointer.
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # if the total is zero, then add the triplet to the result.
                    triplets.append([nums[start], nums[left], nums[right]])
                    # we also increment the left pointer so that we continue 
                    # checking for other triplets, and continue incrementing
                    # the left pointer until the value at left is different
                    # than what it was (same idea as the if statement at the
                    # beginning of this for loop).
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return triplets

        """ Brute force, O(n^4 * log n) """

        # triplets = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         for k in range(len(nums)):
        #             if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = sorted([nums[i], nums[j], nums[k]])
        #                 if triplet not in triplets:
        #                     triplets.append(triplet)
        # return triplets