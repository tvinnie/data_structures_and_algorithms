class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_terms = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_terms:
                return [num_terms[complement],index]
            num_terms[num] = index
        return[]
        