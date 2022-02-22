
print('请输入数字，以，分割')
a=input().split(',')
print('要查找的数字为')
x=int(input())
right=len(a)-1
left=0
found=-1
while left<=right:
    mid=(right+left)//2
    if int(a[mid])>x:
        right=mid-1
    elif int(a[mid])<x:
        left=mid
    else:
        found=mid
        break
print('其下标为{}'.format(found))
        
