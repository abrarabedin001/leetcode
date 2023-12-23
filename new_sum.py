class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                first_num = nums[i]
                second_num = nums[j]
                if (first_num+second_num == target and i!=j):
                    return [i,j]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = {}

        # build hashmap
        for r in range(len(nums)):
            numMap[nums[r]] = r
        
        # find complement
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in numMap and numMap[complement] != i:
                return [i,numMap[complement]]
        return []