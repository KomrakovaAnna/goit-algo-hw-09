def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_counts = {}
    for coin in coins:
        coin_counts[coin] = amount // coin
        amount %= coin
    return coin_counts

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    coin_counts = [float('inf')] * (amount + 1)
    coin_counts[0] = 0
    coin_used = [0] * (amount + 1)
    for amt in range(1, amount + 1):
        for j in range(len(coins)):
            if coins[j] <= amt and 1 + coin_counts[amt - coins[j]] < coin_counts[amt]:
                coin_counts[amt] = 1 + coin_counts[amt - coins[j]]
                coin_used[amt] = coins[j]
    result = {}
    while amount > 0:
        result[coin_used[amount]] = result.get(coin_used[amount], 0) + 1
        amount -= coin_used[amount]
    return result


amount = 113
print("Greedy Algorithm:", find_coins_greedy(amount))
print("Dynamic Programming:", find_min_coins(amount))
