import time
import csv

# 再帰処理を使って実装
def fib_saiki(x):
    if x==1:
        return 1
    if x==2:
        return 1
    return fib_saiki(x-1)+fib_saiki(x-2)

print("input integer")
n = int(input())

# 繰り返し文を使って実装
def fib(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    a = [1,1]
    for i in range(x):
        k = a[i] + a[i+1]
        a.append(k)
    return a[x-1]

# 再帰処理，改良版
"""
a = []
a.append(1)
a.append(1)
a.append(1)
def fib_saiki_imp(x):
    if x==1:
        return 1
    if x==2:
        return 1
    if x<len(a):
        return a[x]
    k = a[x-1] + a[x-2]
    a.append(k)
    return fib_saiki_imp[x-1]+fib_saiki_imp[x-2]
"""

time_1 = time.time()
"""
for i in range(1, n+1):
    fib_saiki(i)
fib_n_saiki = fib_saiki(n)
print("saiki is completed")
"""

time_2 = time.time()

for i in range(1, n+1):
    fib(i)
fib_n = fib(n)
print("nomal_fib is completed")

time_3 = time.time()


"""
for i in range(1, n+1):
    fib_saiki_imp(i)
fib_n_saiki_imp = fib_saiki_imp(n)
print("saiki_imp is completed")

time_4 = time.time()
"""

#print("fib_saiki(n) =", fib_n_saiki, "time:", time_2 - time_1)
#print("fib(n) =", fib_n, "time:", time_3 - time_2)
#print("fib_saiki_imp(n) =", fib_n_saiki_imp, "time:", time_4 - time_3)
print("time:", time_3-time_2)

f = [1,1]
for i in range(2,n+1):
    k = f[i-1] + f[i-2]
    f.append(k)

start = time.time()
#print(f[n-1])
end = time.time()
print("time:", end-start)