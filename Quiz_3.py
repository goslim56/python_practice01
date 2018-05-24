#문제3. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'
list = s[1:len(s)].split("/")
for t in list:
    print("'"+t+"'",end="")
    if list[-1]!=t:
        print(", ",end="")
point = s.rfind("/")+1
print("\n"+s[0:point]+", "+s[point:len(s)])