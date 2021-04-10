class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        l,r = 0,len(nums)-1
        while l<r:
            while l<r and nums[l]%2==1:
                l += 1
            while l<r and nums[r]%2==0:
                r -= 1
            if l<r:
                self.swap(nums,l,r)
        return nums

    def swap(self,nums,l,r):
        tmp = nums[l]
        nums[l] = nums[r]
        nums[r] = tmp
