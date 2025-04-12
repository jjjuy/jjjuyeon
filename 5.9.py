numbers=input('정수를 여러 개 입력하시오:').split() #split()은 입력을 공백으로 나누어 리스트 형태로 저
nums=[]
for i in numbers:
    nums.append(int(i)) #append는 리스트에 요소 추
    
def mean_of_n(nums):
    return sum(nums)/len(nums)

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

print('평균값은', mean_of_n(nums))
print('최댓값은', max_of_n(nums))
print('최솟값은', min_of_n(nums))

