#입력값이 두 개가 아닐 때, 입력값이 숫자가 아닐 때, 입력값이 없을  ->ValueError
try:
    a,b=input('두 수를 입력하시오:').split()
    result=int(a)*int(b)
except ValueError as e:
    print('올바르지 않은 입력입니다. 숫자 두 개를 공백으로 구분해서 입력하세요.')
else:
    print(result)

#0,1,2말고 다른 걸 입력할 때 -> IndexError, 정수가 아닐 때 -> ValueError
a_list=[200,300,400]
print('a_list:',a_list)

try:
    idx=int(input('구하고자 하는 값의 인덱스를 0,1,2 중에서 입력하시오:'))
    result=a_list[idx]
except ValueError:
    print('잘못된 입력입니다. 0,1,2 중 하나를 정수로 입력하세요.')
except IndexError:
    print('입력한 값이 인덱스 범위를 벗어났습니다. 0,1,2 중에서 입력하세요.')
else:
    print('결과:',result)

#존재하지 않는 파일 이름을 입력 -> FileNotFoundError, 파일 접근 권한이 없음 -> PermissionError
try:
    f_name=input('읽어들일 파일 이름을 입력하세요:')
    in_file=open(f_name,'r')
    buf=in_file.readline()
    print(buf)
except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')
except PermissionError:
    print('파일에 접근 권한이 없습니다.')
except Exception as e:
    print('알 수 없는 오류가 발생했습니다:',e)
