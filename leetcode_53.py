class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1,n):
            # 现在的序列加上下一个元素，如果比下个元素本身要大，那就继续往后看，并且记录此时的最大值，以及当前序列的和
            if tmp + nums[i]>nums[i]:
                max_ = max(max_, tmp+nums[i])
                tmp = tmp + nums[i]
                print(tmp,max_)
            else:
            #当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
                max_ = max(max_, tmp, tmp+nums[i], nums[i])
                tmp = nums[i]
        return max_