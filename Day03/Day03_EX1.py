count = 7

def enter():  # enter 함수 선언
    # count = count + 1
    print("지금까지 입장한 고객은 총", count, "명 입니다.")
    print("지금까지 입장한 고객은 총 {}명 입니다.".format(count))

def out():
    print("안녕히 가세요.")

enter()
enter()
enter()
enter()
enter()
out()

