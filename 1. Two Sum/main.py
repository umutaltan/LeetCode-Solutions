from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i]+nums[j] == target:
                    arr.append(i)
                    arr.append(j)
                    return arr