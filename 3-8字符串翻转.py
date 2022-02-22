#python中不支持对已有的字符串赋值
a=str(input())
for i in range(len(a)-1,0-1,-1):
    print(a[i],end="")
