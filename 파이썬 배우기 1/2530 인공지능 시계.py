h, m, s = map(int, input().split())  # 14 30 0
t = int(input())  # 200

s += t  # s=200
m += s//60  # m=33
h += m//60  # h=14
# 시,분,초에 해당값들을 더해주기

s %= 60  # s=20
m %= 60  # m=33
h %= 24  # h=14
# 시간 형태로 바꿔주기

print(h, m, s)  # 14 33 20
