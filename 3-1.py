#输出大于平均值的数据
lst=list(map(int,input().split()))
sum=0
for i in range(0,len(lst)):
    sum=sum+lst[i]
avg=sum/len(lst)
for i in range(0,len(lst)):
    if(lst[i]>avg):
        print('{:d} '.format(lst[i]),end="")