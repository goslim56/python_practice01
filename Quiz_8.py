#문제 8. 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

stack = []

for i in range(5):
    stack.append(int(input()))
sum = 0
for i in stack:
    sum += i

print("평균 : {0}".format(sum/len(stack)))