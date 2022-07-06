t = int(input())
for i in range(t):
    r, s = input().split() #반복횟수, 문자열->ABC
    r = int(r)
    text = "" #빈 문자열 선언
    for i in s: #문자열 길이만큼 반복, i->s[0]~s[2]
        text += r*i
    print(text)
