# https://leetcode.com/problems/isomorphic-strings/description/
""" 
Test Cases:
s = "egg", t = "add" -> Output: true
s = "foo", t = "bar" -> Output: false
s = "paper", t = "title" -> Output: true

s = "ab", t = "cc"  -> Output: false  
Reason: 'a' and 'b' would both need to map to 'c' — violates one-to-one rule.
s = "abab", t = "baba"  ->Output: true  
Reason: 'a' → 'b', 'b' → 'a', pattern holds for all characters.
s = "badc", t = "baba" ->Output: true  
Reason: b mapped to b, at s[2] = d is also mapping to b (t[2]) which is wrong

 """
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        dictt ={}
        for i in range(n):
            if(s[i] in dictt.keys()):
                if(dictt[s[i]] != t[i]):
                    return False
            elif(t[i] in dictt.values()):
                return False
            else:
                dictt[s[i]] = t[i]
        return True

'''
approach: store unique keys from (s) with its values from (t)
also check whether the key is already present in dict if yes -> compare its value with the current value both are same or not?
also check whether the value is already present in dict if yes -> it has already mapped with another key that's y it is existed.
if all checks done at the end -> means passed correctly return Yes
'''