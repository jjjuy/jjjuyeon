src='a2b3c6a2c3f1g1'
output=''

i=0
while i<len(src):
    char=src[i]
    i+=1
    num=''

    while i <len(src) and src[i].isdigit():
        num+=src[i]
        i+=1

    output += char * int(num)
print('src=',src)
print('output=',output)
