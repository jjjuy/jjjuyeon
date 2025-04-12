list1 = [5,6,3,9,2,12,3,8,7]

n = len (list1)
for i in range (n):
    for j in range (n-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]

print('주어진 리스트는=', [5,6,3,9,2,12,3,8,7])
print('정렬된 결과는=', list1)
