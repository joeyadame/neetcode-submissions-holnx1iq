class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        hasDuplicate = False
        for num in nums:
            if num in seen:
                hasDuplicate = True
            seen.add(num)
        return hasDuplicate