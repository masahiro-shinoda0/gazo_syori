import math as m
import time as t

print("input integer")
n = int(input())

start = t.time()

sum = 0
for i in range(1,n):
    sum += (1/(i*i))

end = t.time()

elapsed_time = end - start

sum = sum*6.0
sum = m.sqrt(sum)

print("n:", n, ",", sum)
print("time:", elapsed_time)