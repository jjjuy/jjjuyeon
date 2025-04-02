a=input('5개의 수를 입력하세요:').split()

list1=[]
for num in a:
    list1.append(int(num))

total=sum(list1)
average=total/len(list1)
max_=max(list1)
min_=min(list1)

print('합:',total)
print('평균:',average)
print('최댓값:',max_)
print('최솟값:',min_)
