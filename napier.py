import math as m
import time as t

def kaijo(x):
    if(x==0):
        return 1
    kaijo = 1
    for i in range(x):
        kaijo *= i+1
    return kaijo

print("input integer")
n = int(input())

start = t.time()

sum = 0
for i in range(n):
    sum += (1/kaijo(i))
    # print(i, kaijo(i))



end = t.time()

elapsed_time = end - start

print(sum)

print("n:", n, ",", sum)
print("time:", elapsed_time)