

"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

LC # 643 - Easy
"""
def findMaxAverage(nums, k):
	i = 0
    j = 0
    total = 0
    maximum = float("-inf")
    while i < len(nums):

    	total += nums[i]
        if i+1 >= k:
        	avg = float(total) / float(k)
            maximum = max(maximum,avg)
            total -= nums[j]
            j += 1
        i += 1
    return maximum