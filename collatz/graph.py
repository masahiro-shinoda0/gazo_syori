import matplotlib.pyplot as plt
import csv

a = []
b = []
c = []

with open("output.csv", newline="") as file:
    reader = csv.reader(file)
    print(reader)
    for i in reader:
        #print(i)
        a.append(i)

print("csv reading completed")

for i in range(len(a)):
    k = int(a[i][1])
    b.append(k)
    c.append(i+1)
    #print(b[i])

# グラフの描画
plt.xlabel('number')
plt.ylabel('counting')

plt.title('collatz problems')

plt.scatter(c,b, s=1)

# 画像の保存
plt.savefig("output.png")

plt.show()