import time
import csv

a = []

print("input integer")
n = int(input())

for i in range(n):
    a.append(0)

# コラッツ予想
# 偶数なら2で割る，奇数なら3倍して1足す

for i in range(n):
    k = i+1
    while(k!=1):
        if(k%2 == 0):
            k = k/2
        else:
            k = 3*k + 1

        a[i] += 1

w = []

for i in range(n):
    w.append([i+1, a[i]])
    print(i+1, a[i])

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(w)
print("all writing completed")