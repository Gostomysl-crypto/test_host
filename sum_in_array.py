# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic:
                return [dic[complement], i]
            dic[nums[i]] = i

#print(Solution.twoSum(None, [2,7,11,15], 9))