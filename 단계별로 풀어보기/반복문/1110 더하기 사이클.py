n=int(input()) #68
num=n 
cnt=0 #사이클 수

while True:
    a=num//10 #6 -> n의 십의 자리, '//' -> 정수형 몫 반환
    b=num%10 #8 -> n의 일의 자리
    c=(a+b)%10 #a+b의 일의자리
    num=(b*10)+c #새로운 수

    cnt+=1 #사이클 끝났으면 횟수 추가
    if num==n: #입력받은 수 = 새로운 수
        break

print(cnt)
