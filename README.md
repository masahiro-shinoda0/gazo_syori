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