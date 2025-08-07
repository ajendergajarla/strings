# https://leetcode.com/problems/largest-odd-number-in-string/description/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n-1, -1, -1):
            if(int(num[i])%2==1):
                return num[:i+1]
        return ""
I
""" 
TC: O(N) only 1 iterations check
SC: O(1) No space used
nput: num = "35427"
Output: "35427"

Input: num = "4206"
Output: ""   # No odd digit at end or before

Input: num = "52"
Output: "5"
 """