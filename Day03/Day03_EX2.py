# ---- 지역 변수(if, 함수) ---- #
num = 3
if num == 3:
    apple = 10  # 지역 변수가 아니네요.

print("apple의 값은 {}".format(apple))


def minus(a,b):  # minus라는 이름을 가진 함수를 선언
                 # 이 함수 안에선 a, b를 마음껏 쓰실 수가 있어요.
    banana = 20
    print(a)
    print(b)

minus(3,2)
# print(a) <-- 함수 밖에서는 매개변수는 쓸 수 없습니다.
# print(banana) <-- 함수 안에서 선언한 변수는 밖에서 쓸 수 없습니다.