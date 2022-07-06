n=int(input()) #5
r=1

if n>0: #n값이 0일떈 1출력
    for i in range(1,n+1): #i->1~5 
        r*=i #r=1*1*2*3*4*5

print(r) #120
