# 課題1
# 気温を配列として受け取り，平均気温，最高気温，最低気温を算出

def kion_keisan(t):
    s = 0
    t_min = 100
    t_max = -100
    for i in range(len(t)):
        s += t[i]
        if t_min > t[i]:
            t_min = t[i]
        if t_max  < t[i]:
            t_max = t[i]
    ave = s/len(t)
    r = []
    r.append(ave)
    r.append(t_min)
    r.append(t_max)
    return r

kion = [-3.4, -1.8, -2.9, -3.4, -2.7, -3.7, -3.2, -1.1, 2.2, 5.2, 7.2, 8.1, 9.0, 9.8, 9.4, 8.6, 7.0, 5.8, 5.0, 2.7, 1.6, 2.3, -0.2, -0.8]

k = kion_keisan(kion)
print("average = ", k[0], ", max = ", k[1], ", min = ", k[2])