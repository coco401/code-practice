class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

if __name__ == "__main__":
    nums = [2, 3, 9, 4]
    target = 5
    run = Solution()
    run.twoSum(nums, target)

