from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()

        for i in range(len(nums)):

            # Remove elements outside the window
            if q and q[0] < i - k + 1:
                q.popleft()

            # Remove smaller elements
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Window is ready
            if i >= k - 1:
                output.append(nums[q[0]])

        return output