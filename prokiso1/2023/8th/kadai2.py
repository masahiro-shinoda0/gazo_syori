import mod8th

# 初期化
mod8th.init(12345678)

# 辞書を取得
p2d = mod8th.getPractice2Dict()
print(p2d)

# 文字列を取得
text = mod8th.getPractice2()
print(text)

# p2dに存在するtextをp2dの値で変換し，数値のリストに追加
li = ""
a = []
for i in range(len(text)):
    k = text[i]
    if(k=='-'):
        a.append(li)
        li = ""
        #print("test1")
        continue
    # p2dに存在するかチェック
    for j in p2d:
        if(k==j):
            l = p2d[j]
            li += l
    if i==len(text)-1:
        a.append(li)

print(a)

b = []
for i in range(len(a)):
    k = a[i]
    l = int(k)
    b.append(l)

print(b)

# 平均，最小，最大値を計算
s = 0
b_min = 10000
b_max = -1
for i in range(len(b)):
    s += b[i]
    if(b_min > b[i]):
        b_min = b[i]
    if(b_max < b[i]):
        b_max = b[i]

print("average: ", s/len(b), " max: ", b_max, " min: ", b_min)