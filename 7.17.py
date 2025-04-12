population_A = (100, 150, 230, 120, 180, 100, 140, 95, 81, 21, 4)
population_B = (300, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1)

#(1)
adult_A = population_A[2:] 
adult_B = population_B[2:] 

paper_A = sum(adult_A)
paper_B = sum(adult_B)

print("마을 A와 B에 보낼 투표용지의 개수는 각각", paper_A,'장과 ',paper_B,'장입니다.')
#(2)
old_A=sum(population_A[7:]) 
old_B = sum(population_B[7:])

total_A = sum(population_A)
total_B = sum(population_B)

aging_A = old_A / total_A
aging_B = old_B / total_B

print("마을 A와 B의 고령화 정도는 각각 ",aging_A,'와',aging_B,"입니다.")
