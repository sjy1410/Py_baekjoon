a = list(map(int, input().split())) #정수형 

if a == sorted(a): #순서대로 정렬되있으면
    print('ascending')
elif a == sorted(a, reverse=True): #역순으로 정렬 -> sorted(배열이름, reverse=True)
    print('descending')
else: 
    print('mixed')
