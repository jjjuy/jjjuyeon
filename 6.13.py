n=int(input('n을 입력하세요:'))
a=input(f'{n}개의 수를 입력하세요:').split()
list1=[]
for num in a:
    list1.append(int(num))

total=sum(list1)
mean=total/n
sd=0 #분산 저장할 변수 0으로 초기화
for x in list1: #리스트의 각 숫자에 대해 반복
    sd+=(x-mean)**2 #각 숫자에서 평균을 뺀 후 제곱, sd+=...는 계산한 값을 계속 더함
sd=sd/n #총합을 n으로 나
vyvus=sd**(1/2) #제곱근

print('합:',total)
print('평균:',mean)
print('표준편차:',vyvus)
