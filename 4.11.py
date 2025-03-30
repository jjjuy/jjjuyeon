u=7
b=5
m=0
d=0 #걸린 날 수를 세는 변

while m < 30:
    d += 1
    m = m + u
    print('day:',d,     '달팽이의 위치:',m,'미터')
    if m >= 30:
        print('우물을 탈출하는 데 걸린 날은',d,'일입니다.')
        break #반복문 종료
    m = m - b
    
