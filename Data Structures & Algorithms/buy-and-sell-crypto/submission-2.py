# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # Pseudocode:
#         # 1. Initialize maxProfit to 0.
#         # 2. Try every possible buying day.
#         # 3. For each buying day, try every possible selling day after it.
#         # 4. Calculate the profit for each buy-sell pair.
#         # 5. Update maxProfit if the current profit is greater.
#         # 6. Return maxProfit.

#         maxProfit = 0
#         n = len(prices)

#         for buy in range(n):
#             for sell in range(buy + 1, n):
#                 profit = prices[sell] - prices[buy]
#                 maxProfit = max(maxProfit, profit)

#         return maxProfit

# # Time Complexity: O(n²)
# # Space Complexity: O(1)

#optimized solution
# class Solution:
#     def maxProfit(self,prices:List[int]) -> int:
#         #pseudcode:
#         # 1. Initialize the buying price as the first price
#         # 2. Initialize the maxProfit to 0
#         # 3. Traverse the prices from left to right
#         # 4. If the current price is lower than the buying price, update the buying price
#         # 5. Otherwise calculate the profit by selling today
#         # 6. Update maxProfit if the current profit in greater.
#         # 7. Return maxProfit

#         buy = prices[0]
#         maxProfit = 0

#         for price in prices:
#             if price < buy:
#                 buy = price
#             else:
#                 maxProfit = max(maxProfit, price-buy)
#         return maxProfit
# # Time Complexity: O(n)
# # Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Pseudocode:
        # 1. Use two pointers:
        #    - left = buying day
        #    - right = selling day
        # 2. If selling price is greater than buying price,
        #    calculate the profit and update maxProfit.
        # 3. Otherwise, move the buying pointer to the current day
        #    since it offers a lower buying price.
        # 4. Move the selling pointer forward.
        # 5. Return maxProfit.

        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r

            r += 1

        return maxProfit

# Time Complexity: O(n)
# Space Complexity: O(1)