x=list(input())	#生成一个关于输入的列表
a,b=input().split()	#a,b分别为要查找的字符
x.reverse()	#倒序排列列表
for i in range(0,len(x)):	#遍历列表查找字符并输出,从而从大到小输出索引
    if x[i] == a:
        print(len(x)-i-1,end=' ')
        print(a)
    elif x[i] == b:
        print(len(x)-i-1,end=' ')
        print(b)
