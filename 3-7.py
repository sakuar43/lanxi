a = int(input())
b = list(map(int,input().split()))
if a==len(b):
    print(max(b), b.index(max(b)))
else:
    print('error')

        
        
    
    


