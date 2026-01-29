# 数列の計算
import math

def myPi(n):
    s = 0
    for i in range(n+1):
        s += pow(16, -i)*(4/(8*i+1) - 2/(8*i+4) - 1/(8*i+5) - 1/(8*i+6))
    return s

n = int(input("n = "))
print("sum =", myPi(n))