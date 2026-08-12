class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        fp=0
        for i in range(len(prices)):
            if i<len(discounts):
                val=(prices[i]*(100-discounts[i]))/100
                fp+=val
            else:
                fp+=prices[i]
        return fp
                
        