n=int(input())
for i in range(n):
    s=list(input())
    sum=0
    c=1 #combo
    for i in s:
        if i=='O':
            sum+=c
            c+=1
        else:
            c=1
    print(sum)
