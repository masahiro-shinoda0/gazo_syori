import csv

# encoding="utf-8" で日本語を扱う

# csv 読み込み
with open("sample.csv", newline="") as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)

# csv 書き込み
a = [
    ["anime_name", "kind", "seaon"],
    ["frielen", "fantacy", "2nd"],
    ["jujutu", "action", "3rd"]
]

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(a)