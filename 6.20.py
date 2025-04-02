src='aaaabccccaaaaacccfg'

output=''
if len (src) == 0:
    output=''

elif len(src) == 1:
    output=src+'1'

else:
    count=1

for i in range(1, len(src)):
    if src[i] == src[i-1]:
        count += 1
    else:
        output += src[i-1]+str(count)
        count=1

output += src[-1] +str(count)

print('src=',src)
print('output=',output)
