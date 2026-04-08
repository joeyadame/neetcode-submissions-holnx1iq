class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None]*2*len(nums)
        for i in range(len(nums)*2):
            ans[i] = nums[i-len(nums)]
        return ans
