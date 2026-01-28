# 画像処理
いきなりプログラミングPythonの学習用に作成\
OpenCVを使用

Pythonの仮想環境を構築
```bash
python -m venv .venv
```

## Pythonの基本的な使い方
入出力
```python
# 文字列の出力
print("hello")

# 整数値の入出力
n = int(input())
print(n)

# 改行しない
print(n, end="")
```

繰り返し文
```python
# 1~nまでの逆数の2乗和を足す
sum = 0
for i in range(1,n):
    sum += (1/(i*i))
```

if文
```python
n = int(input())

if n%2 == 0:
    print("even number")
elif n%3 == 0:
    print("multiples of 3 and not even number")
else:
    print("not even number, not multiles of 3")
```

関数
```python
# 階乗を返す関数
def kaijo(x):
    if(x==0):
        return 1
    kaijo = 1
    for i in range(x):
        kaijo *= i+1
    return kaijo
```

再帰処理
```python
# フィボナッチ数列
def fib(x):
    if x==1:
        return 1
    if x==2:
        return 1
    return fib(x-1)+fib(x-2)
```

時間計測
```python
import time

start = time.time()
# 処理
end = time.time()
print("time:", end - start)
```

リスト
```python
# 宣言
a = []

# 要素を追加
a.append(1)
a.append(5,7,9,8,3,2)

# 2番目に3を挿入
a.insert(2,1)

# 要素の削除
a.remove(1)

# 配列の追加
b.append([1,2,3])

# リストの長さ
len(a)

# インデックスと組み合わせる
enumerate(a)

# ソート
sorted(a)
a.sort()
```

二次元リスト
```python
a = []

k = [1,2]
l = [3,4]

# 配列の追加
a.append(k)
a.append(l)
"""
a = [
    [1, 2],
    [3, 4]
]
"""
```

乱数
```python
import random

# 1~100の整数で乱数を生成
n = random.randint(1,100)

# 0~1の浮動小数点数の乱数を生成
m = random.uniform(0,1)
```

グラフ描画
```python
import matplotlib.pyplot as plt

a = [1,2,3,4]
b = [1,2,3,4]

plt.xlabel('x軸')
plt.xlabel('y軸')
plt.plot(a, b)

plt.title('title')

plt.show()
```

csv
```python
import csv

# encoding="utf-8" で日本語を扱う
# csv 読み込み
with open("input.csv", newline="") as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)

# csv 書き込み
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(a)
```