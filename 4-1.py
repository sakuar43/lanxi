error = float(input())
e1, e2 = 1, 2
mul, n = 1, 2
while e2 - e1 >= error:
    mul *= n
    n += 1
    e1, e2 = e2, e2 + 1 / mul
print(f'{e2:.6f}')

