max=0
school=""
t=int(input())
for i in range(t):
    n=int(input())
    for i in range(n):
        name,num=input().split()
        num=int(num)
        if num>max:
            max=num
            school=name
    print(school)
