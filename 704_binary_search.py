class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums.sort()
        left  = 0
        right = len(nums)-1
        center = right//2
        while (right>=left):
            if(nums[center]==target):
                return center
            if(nums[center]>center):
                left = center+1
            else:
                right = center-1
            center = (right+center)//2
        return -1
        