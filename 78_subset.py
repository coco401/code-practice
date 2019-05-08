#双循环
class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums): 
            res += [item+[num] for item in res]
            print(item)
        return res

#dfs
class Solution:

    def subsets(self, nums):
        nums = sorted(nums)
        self.results = []
        self.dfs(nums, [], 0)
        return self.results
    
    def dfs(self, nums, S, index):
        if index == len(nums):
            self.results.append(list(S))
            return
            
        S.append(nums[index])
        self.dfs(nums, S, index + 1)
        S.pop()
        self.dfs(nums, S, index + 1)
        
