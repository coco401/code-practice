class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n != 0:
            self.dfs(n, 0, 0, '', res)
        return res
    def dfs(self, n, left, right, combination, res):
        if right == n:
            res.append(combination)
            return
        if left < n:
            self.dfs(n, left+1, right, combination+"(", res)
        if right < left:
            self.dfs(n, left, right+1, combination+")", res)



