nums=list(map(int,input().split()))
num,cnt=0,0
for x in nums[1:nums[0]+1]:
    if nums.count(x)>cnt:
        num=x
        cnt=nums.count(x)
print(num,cnt)