# 辞書の作成
# 商品をキー，カテゴリを値とする
# 関数input_dict()の作成，商品がある場合はカテゴリを表示

a = {}

a["pen"] = "stationery"
a["mini towel"] = "daily necessities"
a["mask"] = "sanitary producst"
a["tissue"] = "daily necessities"
a["salt"] = "food"

def input_dict(x, k):
    #print("test1")
    for i in x:
        # 中身を表示
        # print(i,":",  x[i])
        #print("test2")
        if(i==k):
            print("category :", x[i])
            return 0
    #print("test4")
    print("the product does not exist")
    return 0

while(1):
    s = input("input product name, ")
    input_dict(a,s)
    n = input("if you want to continue, enter \"y\"\n")
    print("")
    if(n=='y'):
        continue
    else:
        break