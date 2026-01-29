import numpy as np

# 和，個数、平均，最大値，最小値をそれぞれ繰り返し文で実装し，組み込み関数と比較

a = [3,3,3,1,1,2,2,2,3,3,2,3,2,3,3,2,2,1,0,1,2,0,3,0,3,0,1,2,1]

# 和を求める
def wa(x):
    s = 0
    for i in x:
        #print(i, s)
        s = s + i
    return s

# 個数を求める
def kosuu(x):
    c = 0
    for i in x:
        c = c + 1
    return c

# 平均を求める
def heikin(x):
    ave = 0
    c = 0
    for i in x:
        ave = ave + i
        c = c + 1
    ave = ave/c
    return ave

# 最大値を求める
def saidai(x):
    max = 0
    for i in x:
        if(i>max):
            max = i
    return max

# 最小値を求める
def saisyou(x):
    min = 100000
    for i in x:
        if(i<min):
            min = i
    return min

# 組み込み関数と比較
print(wa(a), sum(a))
print(kosuu(a), len(a))
print(heikin(a), sum(a)/len(a))
print(saidai(a), max(a))
print(saisyou(a), min(a))

# 繰り返しで1~100の要素を持つデータを作成，合計値を算出
L = []
for i in range(100):
    L.append(i+1)

sum = 0
for i in range(len(L)):
    sum += L[i]

print("sum =", sum)

# 1~10の整数値乱数を100個生成し，平均を算出


