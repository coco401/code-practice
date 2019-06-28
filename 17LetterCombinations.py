#find all possible results (DFS + backtracking)

#keyboard map
KEYBOARD = {'2':['a','b','c'],
           '3':['d','e','f'],
           '4':['g','h','i'],
           '5':['j','k','l'],
           '6':['m','n','o'],
           '7':['p','q','r','s'],
           '8':['t','u','v'],
           '9':['w','x','y','z']}
class Solution:
    def letterCombinations(self, digits):
        res = []
        #如果digits是空集则返回空
        if digits:
            self.dfs(digits, '', res)
        return res

    def dfs(self, next_digits, combination, res):
        if len(next_digits) == 0:
            res.append(combination)  #deepcopy
        else:
            for letter in KEYBOARD[next_digits[0]]:
                self.dfs(next_digits[1:], combination + letter, res)
        
if __name__ == "__main__":
    s=Solution.letterCombinations
    s("1")