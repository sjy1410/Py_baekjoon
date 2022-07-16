s, k, h = map(int, input().split())

sum = s+k+h
if sum >= 100: #합이 100이상이면
    print('OK')
else:
    if min(s, k, h) == s: #가장 작은 수가 s면
        print('Soongsil') #참여도가 가장 작은
    elif min(s, k, h) == k:
        print('Korea')
    else:
        print('Hanyang')
