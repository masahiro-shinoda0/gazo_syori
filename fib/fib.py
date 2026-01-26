import time

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

time_1 = time.time()
fib_n_saiki = fib_saiki(n)
time_2 = time.time()
fib_n = fib(n)
time_3 = time.time()

print("fib_saiki(n) =", fib_n_saiki, "time:", time_2 - time_1)
print("fib(n) =", fib_n, "time:", time_3 - time_2)

for i in range(1, n+1):
    print(i, fib(i))