n,m=map(int,input().split()) #가로, 세로
#n-1 -> 초콜릿을 1xn의 형태(가로)로 나눔 
#m*(n-1) -> 가로로 나눈 초콜릿들을 세로로 나눔
print(n-1+m*(n-1)) #변수 서로 바꿔도 됨
