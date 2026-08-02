class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        output = []
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash:
                output.append(hash.get(diff))
                output.append(i)
            hash[n] = i

        return output