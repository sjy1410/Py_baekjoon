c = int(input())

for i in range(c):
    s = list(map(int, input().split()))
    avg = sum(s[1:])/s[0]  # 학생 점수들의 합/학생 수

    cnt = 0  # 평균이 넘는 학생들의 수
    for i in s[1:]:
        if i > avg:
            cnt += 1

    per = (cnt/s[0])*100

    print('%.3f' % per+'%')  # 소수점 출력 -> '%.nf'%변수
