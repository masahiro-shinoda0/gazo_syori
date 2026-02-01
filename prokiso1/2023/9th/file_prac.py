# ファイル入出力の練習

# ファイル読み込み
f = open("first-file.txt", "r") # ファイル名，読み込み指示"r"
text = f.read()
f.close()
print(text)


# ファイル出力
# 1行に1つずつ数字を8個記載したファイルを作成，合計値を計算
f = open("first-out.csv", "w") # 書き込み指示"w"
t = ""
f.write("x1, x2, x3, x4, x5, x6, x7, x8\n") # ヘッダ
n = 10
for i in range(n):
    for j in range(8):
        k = str(i*8 + j)
        f.write(k)
        if(j==7): continue
        f.write(", ")
    if(i==n-1): continue
    f.write("\n")
f.close()