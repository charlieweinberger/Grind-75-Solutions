class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # brute force, O(n^2)
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # hash table, O(n)

        hashMap = {nums[0]: 0}
        for i in range(1, len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return [i, hashMap[diff]]
            hashMap[nums[i]] = i