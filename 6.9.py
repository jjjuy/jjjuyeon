n_list=[10,20,30,50,60]
print('리스트 원소들:',n_list)
A=n_list[0]
for a in n_list:
    if a>A:
        A=a
print('리스트 원소들 중 최댓값:', a)
#print('리스트 원소들 중 최댓값:',max(n_list))
