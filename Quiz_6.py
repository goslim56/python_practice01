#문제6.  주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

list = [1,2,3,4,534,5,345,345,34,234,23,213,3126,7,9,44,7,69,67,48,7,95,7,9,0,54,8,9,]

count = 0
sum = 0
for i in list:
    if(i!=0 and i%3==0):
        count+=1
        sum+=i

print("주어진 리스트에서 3의 배수의 개수=> %d"%count)
print("주어진 리스트에서 3의 배수의 합=> %d"%sum)