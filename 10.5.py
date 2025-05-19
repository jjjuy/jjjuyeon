a=1
b=1
c=2
d=3
e=3

x= int (True)
count_1=sum([a is b, a is x, b is x]) +1

y = a+a
z = int(True)+ int(True)

count_2=sum([c is y, c is z, y is z]) +1

count_3=sum([d is e]) +1


print(count_1)
print(count_2)
print(count_3)
