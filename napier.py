import math as m
import time as t
import csv

def kaijo(x):
    if(x==0):
        return 1
    kaijo = 1
    for i in range(x):
        kaijo *= i+1
    return kaijo

print("input integer")
n = int(input())

a = []

start = t.time()

sum = 0
for i in range(n):
    sum += (1/kaijo(i))
    k = [i, sum]
    a.append(k)
    # print(i, kaijo(i))

end = t.time()

elapsed_time = end - start

print(sum)

print("n:", n, ",", sum)
print("time:", elapsed_time)

# 結果をcsvに保存
with open('napier_output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(a)