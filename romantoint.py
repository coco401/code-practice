#字符转换
#13 roman to int (easy)
class Solution:   
    def romanToInt(self, s: str) -> int:
        table = {'I':1, 
				'V':5, 
				'X':10, 
				'L':50, 
				'C': 100, 
				'D':500, 
				'M': 1000}
        prev, res = None, 0
        for char in s:
            curr = table[char]
            res += curr
            if prev and curr > prev:
                res -= 2 * prev
            prev = curr
        return res
		    
	
#12 int to roman (normal)
class Solution:
    def intToRoman(self, num: int) -> str:
        table = {1000: 'M', 
                900: 'CM', 
                500: 'D', 
                400: 'CD', 
                100: 'C', 
                90: 'XC', 
                50: 'L', 
                40: 'XL', 
                10: 'X', 
                9: 'IX', 
                5: 'V', 
                4: 'IV', 
                1: 'I'}
        res = ''
        for k in table:
            while num >= k:
                num -= k
                res += table[k]
        return res
		
#273 Integer to English Words (hard)
class Solution:
    def numberToWords(self, num: int) -> str:
		
	
		
		
		
		
		
		
		
		
