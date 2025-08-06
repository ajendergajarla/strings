# https://leetcode.com/problems/remove-outermost-parentheses/description/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        cnt = 0
        s1 = ""
        
        for i in range(n):
            if(s[i] == "("):
                cnt+=1
                if(cnt>1):
                    s1 += "("

            elif(s[i]==")"):
                cnt-=1
                if(cnt>0):
                    s1 += ")"
       
        return s1
    