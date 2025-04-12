tup=(1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)

clear_list=[]
for i in tup:
    if i not in clear_list:
        clear_list.append(i)

clear_tup = tuple(clear_list)

print('주어진 튜플:',tup)
print('중복 제거 튜플:',clear_tup)
