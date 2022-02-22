m=input()
Str=input()
for i in range(len(Str)):
    if ( m == Str[i]):
        t=True
    if (m!=Str[i]):
        t=False
if (t):
    print("index is",format(i))
else:
    print("Not Found")
    
        
