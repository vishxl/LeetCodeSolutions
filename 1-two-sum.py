class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return False

        ansdict = {}
        
        for i in range(len(nums)):
            if nums[i] in ansdict:
                return [ansdict[nums[i]],i]            
            else:
                ansdict[target - nums[i]]=i