s=input()
abc='abcdefghijklmnopqrstuvwxyz' #알파벳

for i in abc: #i->a~z
    if i in s: #입력받은 단어에 해당 알파벳이 포함되있으면 
        print(s.index(i), end=' ') #그 알파벳 위치출력하고 공백
    else:
        print(-1, end=' ') #아니면 -1 출력하고 공백 
