import math
import time

# 繰り返し文で実装
def kaijo(x):
    if x==1:
        return 1
    k = 1
    for i in range(x):
        k *= i+1
    return k

# 再帰処理で実装
def kaijo_saiki(x):
    if x==1:
        return 1
    return x*kaijo_saiki(x-1)

print("input integer")
n = int(input())

time_1 = time.time()
kaijo_n = kaijo(n)
time_2 = time.time()
kaijo_saiki_n = kaijo_saiki(n)
time_3 = time.time()

print("kaijo =", kaijo_n, "time:", time_2 - time_1)
print("kaijo_saiki =", kaijo_saiki_n, "time:", time_3 - time_2)