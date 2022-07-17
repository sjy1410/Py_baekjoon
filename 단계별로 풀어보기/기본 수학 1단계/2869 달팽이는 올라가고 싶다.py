import sys
import math

a, b, v = map(int, sys.stdin.readline().split())
# 낮에 올라가는 미터, 밤에 미끄러떨어지는 미터, 올라야할 나무막대의 높이
day = (v-b)/(a-b)
# v/a-b라 하면 정상에 가도 밤에 다시 내려갈 수 있다.
# 그러므로 정상에 한번 도달하면 밤에 미끄러지지 않는 것을 고려해 분자값을 v-b로 준다.
print(math.ceil(day))  
# (v-b)/(a-b)의 형태는 소수점 값이 나오는데 5.0은 5일이 걸리는 것이지만 5.2는 6일이 걸리는 것이기 때문이다.
# 그 때문에 걸린 날짜의 소수점을 올림처리해서 처리한다.

'''
a, b, v = map(int, input().split())

c = 0  # 올라가는데 걸리는 일수
s = 0  # 달팽이가 오른 미터의 합
while 1:
    s += a
    c += 1
    if v == s:
        break
    s -= b

print(c)

시간초과가 걸림
'''
