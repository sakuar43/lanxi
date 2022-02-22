from cgitb import reset


s=input()
res=0
for i in range(len(s)):
    if s[i]>='0' and s[i]<='9':
        res=res*10+int(s[i])
print(res)        
    