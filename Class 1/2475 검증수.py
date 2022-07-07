sum = 0
n = list(map(int, input().split()))
for i in n:
    sum += i**2
print(sum % 10)

#숫자 여러개를 한 줄에 입력받을 땐 배열사용
