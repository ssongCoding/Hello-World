win = {
    "가위" : "바위",
    "바위" : "보",
    "보" : "가위"
}

while True:
    user1 = input()  # 상대
    user2 = input()  # 나

    # 조건 자리에 변수 1개만 두면, = 그 변수에 값이 0이 아니면 다 참
    if user1 == "그만" or user2 == "그만":
        print("게임을 종료합니다.")
        break

    if win[user1] == user2:
        print("와 이겼다!")  # user2가 이겨야 하는거죠.
    elif win[user2] == user1:  # user2가 "아이고 졌다!"
        print("아이고 졌다!")    # user1이 이긴다는 소리
    else:  # 이기지도 지지도 않았으니까,
        print("비겼다!")