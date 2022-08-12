
# 기능 : 정수 2개, 그 2개를 곱해서 저한테 돌려주세요.
# 그러고 저는 돌려받은 값을 result 상자에 담고, result를 출력할게요.
def func1(n1, n2):
    return n1 * n2

result = 20 # n1 = 2, n2 = 10
print(result)


# 매개변수로 돈을 전달하면, 2배로 돌려주는 함수
def double(m):  # m = 1000
    return m * 2  # return 2000

money = 1000

money = double(money)
print(money)