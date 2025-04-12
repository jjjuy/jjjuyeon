def birthday(id_num):
    year = int(id_num[:2])
    month = int(id_num[2:4])
    day = int(id_num[4:6])

    if year >= 50:
        year += 1900
    else:
        year += 2000

    return str(year)+'년 '+str(month)+'월 '+str(day)+'일 '

input_id = input('주민등록번호 첫 6숫자 형식 입력:')
result = birthday(input_id)
print(result)
