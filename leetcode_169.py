class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        nums.sort()
        q=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                q+=1
            else:
                q=1
            if q>len(nums)/2:
                return nums[i]
				
				
				
				
#哈希表

class Solution:
    def majorityElement(self, nums):
        counts = {}
        for i in nums:
            if i in counts.keys():
                counts[i] += 1
            else:
                counts[i] = 1
        
        return max(counts.keys(), key=lambda x: counts[x])
		
#排序 因为一半都是这个数，所以中间的那个数一定是众数

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
		
		
		
		
#随机数 
import random

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
				
				
#投票法


class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for i in range(len(nums)):
            if count == 0:
                c=i
                candidate = nums[i]
            count += (1 if nums[i] == candidate else -1)
            if count>i-c+1:
                return candidate
        return candidate

