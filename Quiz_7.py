#문제7.키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전
# 각 몇 개로 변환 되는지 작성하시오.
count={"50000":0, "10000":0, "5000":0, "1000":0, "500":0, "100":0, "50":0, "10":0, "5":0, "1":0}
cash = list(count.keys())
num = input("금액:")
if(num.isdigit()):
    num = int(num)
    i=0
    while num>0:
        if num>=int(cash[i]):
            num-=int(cash[i])
            count[cash[i]]+=1
        else:
            i+=1
for k,v in count.items():
    print('{0}원: {1}개'.format(k, v))
