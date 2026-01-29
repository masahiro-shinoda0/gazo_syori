import mod8th
import math

# 初期化
mod8th.init(12345678)

# 辞書を取得
a = mod8th.getPractice1()

# 平均，標準偏差を計算
s = 0
for i in a:
    k = a[i]
    s += k
average = s/len(a)

b = 0
for i in a:
    k = (a[i] - average)*(a[i] - average)
    b += k
dispersion = math.sqrt(b/len(a))

print("average: ", average, " dispersion: ", dispersion)

# 最大，最小値について値とキーを出力
mins = 10000
minp = ""
maxs = -1
maxp = ""
for i in a:
    #print("test1")

    if mins > a[i]:
        #print("test2")
        mins = a[i]
        minp = i
    if maxs < a[i]:
        #print("test3")
        maxs = a[i]
        maxp = i

# なぜかエラー -> なおった
print("max: ", maxp, a[maxp], " min: ", minp, a[minp])