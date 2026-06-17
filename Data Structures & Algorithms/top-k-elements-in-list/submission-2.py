# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}

#         for num in nums:
#             count[num] = count.get(num, 0) + 1

#         sorted_nums = sorted(count.items(), key=lambda x: x[1], reverse=True)

#         return [num for num, freq in sorted_nums[:k]]
# 2nd sol as per video
class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res