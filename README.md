# 画像処理
いきなりプログラミングPythonの学習用に作成\
OpenCVを使用

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

時間計測
```python
import time as t

start = t.time()
# 処理
end = t.time()
print("time:", start - end)
```

配列
```python
# 空の配列
a = []

# 要素を追加
a.append(1)

# 配列の追加
a.append([1,2,3])
```

乱数
```python
import random as r

# 1~100の整数で乱数を生成
n = r.randint(1,100)
```

グラフ描画
```python
import matplotlib.pyplot as plt
a = [1,2,3,4]
plt.plot(a)
plt.show()
```