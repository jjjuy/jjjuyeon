#4.7
n=int(input('숫자를 입력하세요:'))
is_prime=True
for a in range (2,n):
    if (n%a==0):
        is_prime=False
        break

if (is_prime):
      print(n,'는 소수입니다')
else:
    print(n,'는 소수가 아닙니다')
