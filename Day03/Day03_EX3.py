
def sumNum(n1, n2, n3):
    num = n1 + n2 + n3
    return num

res = sumNum(2,3,4)  # 함수가 return 값이 있으면, 통째로 그 값으로
                     # 치환(대체) 할거에요.
print(res)  # <-- 9


numnum = 7

def numPrint():
    global numnum # 함수 안에서 전역변수 numnum의 값에 접근하겠다고 알려줌
    numnum = 10   # 전역변수 numnum과 전혀 관계가 없는
                  # 새로운 지역변수 numnum을 선언

numPrint()
print("numnum의 값은 {}입니다.".format(numnum))
