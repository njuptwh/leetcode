#我的代码
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[1]<nums[0]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        score = {}
        score[0] =0 
        c=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c+=1
                score[i]=c
            else:
                c-=1
                score[i]=c
            if i>=2 and score[i] == score[i-2] and score[i]<score[i-1]:
                return i-1
				
#别人的代码

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return i-1
        return len(nums)-1