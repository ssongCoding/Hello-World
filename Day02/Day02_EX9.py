
def buySnack(m):
    return m - 1000


print("주머니에 있는 돈이 얼마인가요?")
money = input()  # input() 함수는 return값이 string(문자열)
# print(type(money))  # type() 함수는, return :
                    # 매개변수로 받은 값이 어떤 자료형인지
imoney = int(money)  # int() 함수는,
                     # 매개변수로 받은 변수 안에 들어있는 값을
                     # integer(정수)로 바꿔서 return
# print(type(imoney))
imoney = buySnack(imoney)
print(imoney)  # 입력한 값 - 1000
