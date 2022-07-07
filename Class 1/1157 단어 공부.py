w = input().upper() # Mississipi -> MISSISSIPI / zZa
w_list=list(set(w)) # w_list = [M, I, S, P] / [Z, A]
cnt=[]

for i in w_list:
    count=w.count(i)
    cnt.append(count) # cnt = [1, 4, 4 ,1] / [2, 1]

if cnt.count(max(cnt))>=2: #cnt 배열에서 가장 큰 값이 2개 이상
    print("?")
else:
    print(w_list[cnt.index(max(cnt))]) #w_list[1]
    #w_list에서 cnt의 가장 큰 수가 위치한 배열의 위치에 있는값을 출력
