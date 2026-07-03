class Solution:
    def maxArea(self, heights: List[int]) -> int:
    # brute force approach
        res = 0

        for i in range(len(height)):
            for r in range(l+1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res,area)
        return res
