class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        #无需辅助数组的方法
        n = len(nums)
        for i in range(n):
            while nums[i]!=i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                tmp = nums[i]
                nums[i] = nums[tmp]
                nums[tmp] = tmp
        return None


