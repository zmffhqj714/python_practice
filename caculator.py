print("첫번째 숫자를 입력해 주세요")
x = int(input())
print("두번쨰 숫자를 입력해 주세요")
y = int(input())
print("원하는 연산을 선택해 주세요")
print("1. 더하기 2. 빼기 \n3. 곱하기 4. 나누기")
z = int(input())

if z == 1:
    print(str(x) + " + " + str(y) + " = " + str(x + y))
elif z == 2:
    print(str(x) + " - " + str(y) + " = " + str(x - y))
elif z == 3:
    print(str(x) + " x " + str(y) + " = " + str(x * y))
elif z == 4:
    print(str(x) + " ÷ " + str(y) + " = " + str(x / y))

