# Given an integer array nums, 
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=0
        n=len(nums)
        while(i<n):
            if nums[i]==0:
                j=i
                while(j<n):
                    if nums[j]!=0:
                        nums[i],nums[j]=nums[j],nums[i]
                        j=n
                    else:
                        j+=1
                        
            i+=1