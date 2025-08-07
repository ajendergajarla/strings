# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_strs = len(strs)
        shortest_element = min(strs, key=len)
        for i in range(len(shortest_element)):
            prefix = shortest_element[i]
            for j in range(len_strs):
                if(strs[j][i]!=prefix):
                    return strs[j][:i]
        return shortest_element
    

"""
TC: O(N)
SC: O(1)

Input: ["flower", "flow", "flight"]
Output: "fl"

Input: ["dog", "racecar", "car"]
Output: ""

Input: ["flower", "flowers"]
Output: "flower"
"""