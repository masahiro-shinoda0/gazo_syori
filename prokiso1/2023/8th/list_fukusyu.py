import numpy as np

# 和，個数、平均，最大値，最小値をそれぞれ繰り返し文で実装し，組み込み関数と比較
print("kadai1")
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
print("")

# 繰り返しで1~100の要素を持つデータを作成，合計値を算出
print("kadai2")
L = []
for i in range(100):
    L.append(i+1)

sum = 0
for i in range(len(L)):
    sum += L[i]

print("sum =", sum)
print("")

# 1~10の整数値乱数を100個生成し，平均を算出
print("kadai3")
x = []
for i in range(100):
    r = np.random.randint(1,10)
    x.append(r)

print(x)

s = 0
for i in range(len(x)):
    s += x[i]

print("sum=", s/len(x))
print("")

# 文字列を数値のリストに変換し，平均値を算出
print("kadai4")
moji = "12-14-14-19-21-18-15-23-9-26-26-14-13-8-9-13-3-17-16-2-17"

b = []

s = 0
li = ""
for i in range(len(moji)):
    k = moji[i]
    if(k=='-'):
        s = int(li)
        b.append(s)
        s = 0
        li = ""
        continue
    if i==len(moji)-1:
        li += k
        s = int(li)
        b.append(s)
    li += k

print(b)
k = 0
for i in range(len(b)):
    k += b[i]
print("sum=", k/len(b))