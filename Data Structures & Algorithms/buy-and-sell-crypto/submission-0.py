class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Pseudocode:
        # 1. Initialize maxProfit to 0.
        # 2. Try every possible buying day.
        # 3. For each buying day, try every possible selling day after it.
        # 4. Calculate the profit for each buy-sell pair.
        # 5. Update maxProfit if the current profit is greater.
        # 6. Return maxProfit.

        maxProfit = 0
        n = len(prices)

        for buy in range(n):
            for sell in range(buy + 1, n):
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)

        return maxProfit

# Time Complexity: O(n²)
# Space Complexity: O(1)