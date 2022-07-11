croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] #크로아티아 문자를 담은 배열
s = input()

for i in croatia: 
    s = s.replace(i, '#') #s에 croatia배열에 있는 문자가 있다면 #으로 교체
print(len(s)) # 변환된 s길이(크로아티아 알파벳 개수) 출력

#s = ljes=njak = #e##ak
