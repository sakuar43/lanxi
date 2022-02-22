n = int(input())
flag = True
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 前十七位数权重
M = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]  # 最后一位检验数
for i in range(0, n):
    t = list(input())
    integer = [int(t[i]) * weight[i] if '0' <= t[i] <= '9' else -100000 for i in range(0, 17)]
    z = sum(integer) % 11  # 前十七位数×权重÷11的检验数
    if t[-1] != "X":
        if z < 0 or M[z] != int(t[-1]):
            flag = False
            print("".join(t))
    else:
        if z != 2:
            flag = False
            print("".join(t))
if flag ==True:
    print("All passed")
