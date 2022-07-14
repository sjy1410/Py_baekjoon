import sys
input = sys.stdin.readline #컴파일 시간 줄이기

n = int(input())

# 대각선으로 줄을 나누면(지그재그) [1/1], [1/2,2/1], [3/1,2/2,1/3] .. 이런식으로 나타낼 수 있다.

line = 1  # 라인
while n > line:  # n에서 line을 1씩 늘려가며 빼면 n이 몇번째 라인인지 구할 수 있다.
    n -= line
    line += 1

if line % 2 == 0:  # 짝수라인 일땐
    s = n  # 분자는 1부터 n까지 늘고
    m = line-n+1  # 분모는 n부터 1까지 준다

else:  # 홀수 라인은 짝수라인의 반대
    s = line-n+1
    m = n

print(s, m, sep='/')  # 값 사이 '/'추가
