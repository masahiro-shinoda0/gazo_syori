# 正規分布を表現したい

import random as r
import matplotlib.pyplot as plt

a = []
b = []
c = []

n = 100

for i in range(n):
    a.append(0)
    b.append(0)
    c.append(0)

"""
print(a)
for i in range(n):
    k = r.randint(1,100)
    a[k-1] += 1

print(a)


for i in range(n):
    k = r.randint(1,100)
    l = r.randint(1,100)
    ave = int((k+l)/2)
    b[ave-1] += 1

print(b)
"""


for i in range(n):
    sum = 0
    for j in range(n):
        k = r.randint(1,100)
        sum += k
    ave = int(sum/n)
    c[ave-1] += 1

print(c)

# 動かない
#plt.plot(c, label='first')
#plt.show()

"""
for i in range(100):
    print(".", end="")
    for j in range(c[i]):
        print("#", end="")
    print()
"""


d = []
N = 100000

for i in range(N):
    d.append(0)

for i in range(N):
    sum = 0
    for j in range(100):
        k = r.randint(1,6)
        sum += k
    ave = int(sum/100)
    d[ave-1] += 1

"""
for i in range(100):
    print(".", end="")
    for j in range(int(d[i]/100)):
        print("#", end="")
    print()
"""

plt.plot(d, label='nd')
plt.show()