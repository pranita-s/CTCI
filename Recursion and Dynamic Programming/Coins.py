# TIME - O(coins * amount)
# SPACE - O(amount)


def coinChange(coins, amount):
    dp=[0]+[float('inf')]*amount
    for coin in coins:
        for amt in range(1,amount+1):
            if amt >= coin:
                dp[amt] = min(1+dp[amt-coin],dp[amt])

    return dp[-1]


print(coinChange([1,2,5],11))
