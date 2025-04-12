import random as rd
a=rd.randint(1,20)

n=0

while True:
    i=int(input('1~20까지의 숫자를 입력하세요:'))
    n+=1
    if a > i:
        print(i,'보다 큽니다!')
    elif a < i:
        print(i, '보다 작습니다!')
    else:
        if n <= 3:
            print('정답입니다!',n,'번만에 맞춘 당신은 천재!')
        elif 4 <= n <= 6:
            print('정답입니다!',n,'번만에 맞추셨네요. 잘했어요^^')
        else:
            print('정답입니다!',n,'번만에 맞추다니 쩝쩝...')
        break



