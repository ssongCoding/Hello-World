
# 기능 : 가나다라마바사 출력
def ganada():
    print("가나다라마바사")

ganada()
ganada()
ganada()


# 기능 : 정수 1개를 받을거구요. 받은 정수를 출력
def printNum(n1):
    print(n1)

printNum(309)  # n1 = 309


# 기능 : 정수 2개, 그 숫자 2개를 곱한 값을 출력
def multiPrint(n1, n2):
    print(n1*n2)

num1 = 3
num2 = 7

multiPrint(num1, num2)  # n1 = 3, n2 = 7


# 기능 : 정수 1개를 받아서, 그 정수를 *7을 해서 저한테 돌려줄거에요.
def seven(num):
    return num * 7
    #res = num * 7
    #return res

result = seven(8)
print(result)

