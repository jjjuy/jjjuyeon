import datetime as dt
#(1)
start=dt.date(2019,2,14)
today=dt.date.today()
days=(today-start).days

print('춘향이와 몽룡이의 연애 시작일:',start.year,'년',start.month,'월',start.day,'일')
print('연애 시작일로부터 경과한 날짜:',days,'일')

#(2)
annis=[100,200,500,1000]
for anni in annis:
    ani=start+dt.timedelta(days=anni)
    print(anni,'일 기념일:', ani.year,'년',ani.month,'월',ani.day,'일')
