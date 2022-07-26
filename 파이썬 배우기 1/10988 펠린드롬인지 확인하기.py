w=list(str(input())) #reverse함수를 적용하기 위해 단어를 문자열 배열로 받는다

if list(reversed(w))==w: #함수를 적용한 단어를 비교할 단어와 같은 배열로 만들어준다
    print('1')
else:
    print('0')
