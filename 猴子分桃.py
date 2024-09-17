def calculate_peaches(n, m):
    peaches = m
    for i in range(n, 0, -1):
        peaches = (peaches + 1) * 2
    return peaches

# 对于10只猴子的情况
n1 = 10
m1 = 2
print(f"原本有 {calculate_peaches(n1, m1)} 个桃子。")

# 对于100只猴子的情况
n2 = 100
m2 = 2
print(f"原本有 {calculate_peaches(n2, m2)} 个桃子。")

'''
input  : n -> 第n号猴
       : m -> 剩下m个桃子
output : 原本桃子的个数
'''