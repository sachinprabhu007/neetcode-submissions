# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}

#         for i, num in enumerate(nums):
#             complement = target - num

#             if complement in seen:
#                 return [seen[complement], i]

#             seen[num] = i

# Solution as per video
class Solution: 
    def twoSum(self, nums: List[int], target:int ) -> List[int]:
        prevMap = {} # val :index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i