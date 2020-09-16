class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return nums[i+1]
            
        return nums[0]
