class Solution:
    def maxArea(self, heights: List[int]) -> int:
    # brute force approach
        res = 0

        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                area = (r - l) * min(heights[l], height[r])
                res = max(res,area)
        return res
