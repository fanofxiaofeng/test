#!/usr/bin/python

class Solution:
	# @param {integer[]} nums
	# @return {integer[]}
	def productExceptSelf(self, nums):
		ans = [1] * len(nums)
		right = 1
		for i in range(1, len(ans)):
			ans[i] = ans[i - 1] * nums[i - 1]
		for i in range(len(ans) - 2, -1, -1):
			right *= nums[i + 1]
			ans[i] *= right
		return ans

s = Solution()
print s.productExceptSelf([5,2,3,4])

