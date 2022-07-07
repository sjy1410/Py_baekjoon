n=int(input())
s=list(map(int,input().split())) 
m=max(s)

new=[]
for i in s: #s의 배열길이 만큼 반복
    new.append(i/m*100) #값 조작한 거 새 배열에 추가

print(sum(new)/n) #조작한 값들의 평균
