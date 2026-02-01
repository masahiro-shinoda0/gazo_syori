# file_prac.pyで作成した"first-out.csv"を読み込んで，合計値を計算する

f = open("first-out.csv", "r") # ファイル名，読み込み指示"r"
text = f.read()
f.close()

w = ""
sum = 0
for i in text: # textには1文字ずつ読み込まれている
    k = text
    if(k=="," or k==" "):
        sum += int(w)
        w=""
        continue
    w += k
    #print(i)

print(sum)

# test
#print(text)