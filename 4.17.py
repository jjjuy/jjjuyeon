for a in range(1, 20001):  # a를 1부터 20000까지 반복
    sum_i = 0  # a의 진약수 합을 저장할 변수
    # a의 진약수 합 구하기
    for i in range(1, a):  # 1부터 a-1까지 반복
        if a % i == 0:  # i가 a의 약수이면
            sum_i += i  # sum_i에 더하기

    sum_j = 0  # sum_i의 진약수 합을 저장할 변수
    # sum_i의 진약수 합 구하기
    for j in range(1, sum_i):  # 1부터 sum_i-1까지 반복
        if sum_i % j == 0:  # j가 sum_i의 약수이면
            sum_j += j  # sum_j에 더하기

    # a와 sum_i가 친화수인지 확인
    if sum_j == a and a != sum_i:  # sum_j가 a와 같고, 자기 자신과 친화수가 아니면
        print(a,'의 친화수',sum_i)
                        
