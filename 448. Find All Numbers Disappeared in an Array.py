class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            idx=abs(n)-1
            if nums[idx]>0:
                nums[idx]=nums[idx]*-1
                        
            
        return [i+1 for i in range(len(nums)) if nums[i]>0]
