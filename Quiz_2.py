#문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.
while True:
    num = input("수를 입력하세요: ")
    if(num=="0"):
        break
    if num.isdigit():
        num = int(num)
        if(num%2==0):
            print("짝수")
        else:
            print("홀수")
    else:
        print("정수가 아닙니다.")
    print("Process finished with exit code 0")