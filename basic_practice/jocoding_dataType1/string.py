#문자열 출력
a = "Hello world"
#c언어와 비슷하게 문자열의 요소마다 0부터 인덱스를 부여함.
for i in range(len(a)): #len(a)는 a의 길이를 반환함.
    print(a[i], end=' ')
#end = ' '는 print문이 끝날 때 줄바꿈을 하지 않고 공백을 출력하게 한다.
print()
for i in range(5):
    print(a[i], end=' ')

print(a[:8]) #Hello wo
print(a[1:8]) #ello wo
print(a[1:]) #ello world
print(a[:]) #Hello world
print(a[::2]) #Hlowrd
print(a[::-1]) #dlrow olleH
print(a[2::2]) #lowrd
#[이상:미만:간격:]꼴로 써 사용할 수 있다.