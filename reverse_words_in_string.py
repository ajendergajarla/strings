# https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        s1=""
        start = -1
        n = len(s)
        for i in range(n):
            if(start==-1 and s[i]==" "):
                continue
            elif(type(s[i]) is str and start==-1):
                start = i
            elif(s[i]==" " and start!=-1):
                s1 = s[start:i] + " " + s1
                start = -1
        if(start!=-1):
            s1 =  s[start:] + " " + s1
        s1 = s1.strip()
        return s1

# https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1

class Solution:
    def reverseWords(self, s):
        # code here
        s1=""
        start = -1
        n = len(s)
        if('.' not in s): return s
        for i in range(n):
            
            if(start==-1 and s[i]=="."):
                continue
            elif(type(s[i]) is str and start==-1):
                start = i
            elif(s[i]=="." and start!=-1):
                if(len(s1)==0):
                        s1 = s1 + s[start:i]
                else:
                    s1 = s[start:i] + "." + s1
                start = -1
        if(start!=-1):
            if(len(s1)!=0): s1 =  s[start:] + "." + s1
            else: s1 = s1+ s[start:]
        return s1
        
    