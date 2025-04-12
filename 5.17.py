def sum_range(n1,n2):
    list1=[]
    for n in range (n1,n2+1):
        list1.append(n)
    return sum(list1)

print('10에서 20까지의 정수의 합:',sum_range(10,20))
print('40에서 100까지의 정수의 합:',sum_range(40,100))
