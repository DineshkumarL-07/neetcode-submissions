class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for n in range(len(nums)):
            val = target - nums[n]
            if val in hashMap:
                return [hashMap[val], n]
            hashMap[nums[n]] = n