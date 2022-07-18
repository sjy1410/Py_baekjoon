a = list(map(int, input().split()))
a.sort()
for i in range(len(a)): #range(3)으로 해도 됨
    print(a[i], end=' ')
