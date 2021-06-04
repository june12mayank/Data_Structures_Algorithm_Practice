#Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        i=0
        while(i<len(nums)-1):
            if nums[i]!=nums[i+1]:
                return nums[i]
            else:
                i+=2
        return nums[len(nums)-1]
            