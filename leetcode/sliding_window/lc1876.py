

"""
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

LC # 1876 - Easy
"""
def countGoodSubstrings(s):
	"""
    :type s: str
    :rtype: int
    """

    res = 0
    while i < len(s)-2:

    	if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
                res += 1
        i += 1
    return res

def main():
    print(countGoodSubstrings("xyzzaz"))
    print(countGoodSubstrings("aababcabc"))

if __name__ == "__main__":
    main()