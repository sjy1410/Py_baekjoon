while True: #계속해서 반복한다
    try: #계속해서 입력받다가
        print(input())
    except EOFError: #입력값이 안들어온다면 
        break #while문 종료
