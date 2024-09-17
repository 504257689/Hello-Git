def count_ways(n, coins, memo):
    if n == 0:
        return 1  
    if n < 0 or not coins:
        return 0  
    if memo[n] != -1:
        return memo[n]  
    
    count = 0
    for i in range(n//coins[0] + 1):
        count += count_ways(n - i * coins[0], coins, memo)
    memo[n] = count
    return count

# 输入金额（单位：分）
n = int(input("请输入金额（单位：分）: "))
coins = [1, 2, 5]  
memo = [-1] * (n + 1)  # 备忘录
print(count_ways(n, coins, memo))
