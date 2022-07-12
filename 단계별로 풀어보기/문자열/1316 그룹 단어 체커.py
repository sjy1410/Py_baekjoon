n = int(input())
cnt = n #일단 입력 될 단어수만큼 그룹단어수 설정

for i in range(n):
    s = input()
    for j in range(0, len(s)-1): #배열이니까 0번지 부터
        if s[j] == s[j+1]: #문자 두 개 이상 연속해서 나타나면
            pass #for문 계속 실행
        elif s[j] in s[j+1:]: #문자가 연속되지 않으면(한 문자가 다다음 문자들의 배열에 속해있으면)
            cnt -= 1 #그룹단어 수에서 1을 빼고(그룹단어에서 제외)
            break #for문 종료

print(cnt)
