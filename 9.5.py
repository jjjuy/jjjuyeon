f=open('number1to10.txt','w')

for a in range(1,11):
    f.write(str(a)+'\n')
    
f.close()
