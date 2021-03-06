#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

#Example 1:
#Input: digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


output=[]
c=0
class Solution(object):
    def letterCombinations(self, digits):
        global c, output
        """
        :type digits: str
        :rtype: List[str]
        """
        if(digits==""):
            return []
        nums=list(digits)
 
        def getCombinations(lst):
            global output,c
            if(c==0):
                c+=1
                for x in lst:
                    for y in x:
                        output.append(y)
            else:
                temp=output
                output=[]
                for i in range(len(temp)):
                    for y in lst:
                        output.append(temp[i]+y)
        begin=0                
        for x in nums:
            if(begin==0):
                c=0
                output=[]
                begin +=1
            chars=[]
            jump=3* (int(x)-2)
            start=97+jump
            loop= int(x)==9 and 4 or int(x)==7 and 4 or 3
            add= int(x) >7 and 1 or 0
            for z in range(loop):
                chars.append(chr(start+z+add))
            getCombinations(chars)
        return output
