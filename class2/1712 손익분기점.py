a, b, c = map(int, input().split()) # 고정비용, 생산비용(1대), 판매가격(1대)

if b >= c:  # 판매 가격이 생산 비용보다 작거나 같으면
    print('-1')  # 손익분기점 발생 안됨
else:
    print(a//(c-b)+1) #손익분기점 = (고정비용//순 이익)+1
    #고정비용//순 이익 = 수입과 비용이 같아지는 시점
