#!/usr/bin/env python
# Author: Brian Vaughan
# Date: June 11th 2021

# Test Input
nums = [2,7,11,15]
target = 9 

# Inital Solution
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if(target == nums[i]+nums[j]):
                    return([i, j])

# # Faster Solution (not mine)
# class Solution(object):
#     def twoSum(self, nums, target):
#         check = {}
#         for i, v in enumerate(nums):
#             remaining = target-v
#             if remaining in check:
#                 return [check[remaining], i]
#             check[v] = i


test = Solution()
print(test.twoSum(nums, target))