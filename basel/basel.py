import math as m
import time as t
import csv

print("input integer")
n = int(input())

a = []

start = t.time()

sum = 0
for i in range(1,n):
    sum += (1/(i*i))
    k = sum
    k *= 6.0
    k = m.sqrt(k)
    l = [i, k]
    a.append(l)

end = t.time()

elapsed_time = end - start

sum = sum*6.0
sum = m.sqrt(sum)

print("n:", n, ",", sum)
print("time:", elapsed_time)

with open("basel_output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(a)