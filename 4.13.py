#암스트롱 수 구하기...
print('세 자리의 암스트롱 수:', end=" ") # end=" "는 줄바꿈!
for i in range (100, 1000):
    hundreds = i // 100
    tens = (i % 100) // 10
    ones = i % 10
    if i == hundreds**3 + tens**3 + ones**3:
        print(i, end=" ")
