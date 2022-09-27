

"""
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

LC # 2379 - Easy
"""

class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        i = 0
        j = 0
        minimum = float("inf")
        count = 0
        while i < len(blocks):
            if blocks[i] == 'W':
                count += 1
            if i + 1 >= k:
                minimum = min(minimum,count)
                if blocks[j] == 'W':
                    count -= 1
                j += 1
            i += 1
        return minimum