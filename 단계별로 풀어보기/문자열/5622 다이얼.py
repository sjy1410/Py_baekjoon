dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()

n = 0 #최소 시간
for i in range(len(a)):  # i = 문자열 a의 길이만큼
    for j in dial:  # j = ABC~WXYZ
        if a[i] in j: #a[i]가 dial에 속해 있으면
            n += dial.index(j)+3 
            #배열은 0번지부터 시작하므로 1초, 1번에 거는데 2초가 필요하므로 총 3(초)을 더해준다
print(n)
