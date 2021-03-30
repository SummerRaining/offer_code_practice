class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left,right = 0,len(numbers)-1
        if numbers[left]<numbers[right]:
            return numbers[left]

        while right>left+1:
            mid = int((left+right)/2)
            if numbers[mid]==numbers[left] and numbers[mid]==numbers[right]:
                return self.helper(numbers,left,right)
            if numbers[mid]>=numbers[left]:
                left = mid
            else:
                right = mid
        return numbers[right]

    def helper(self,numbers,left,right):
        min = numbers[left]
        for i in numbers[left:right+1]:
            if i<min:
                min = i
        return min



