n=int(input()) # 참가하는 사람 수
p_list=[] #빈 배열 생성

for i in range(n): #만큼 반복
    a, b, c=map(int,input().split())

    if a==b and b==c:
        money=10000+a*1000
    elif a==b:
        money=1000+a*100
    elif a==c:
        money=1000+a*100
    elif b==c:
        money=1000+b*100 #b로 바꿔준다
    else:
        money=max(a,b,c)*100 #여기까지 for문에서 조건문 돌리고
    p_list.append(money) #나온 money값 배열에 추가

print(max(p_list)) #배열에서 가장 큰 값 출력
