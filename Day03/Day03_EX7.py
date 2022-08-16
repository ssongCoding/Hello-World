music = "on"

n = 0  # 바퀴 수
while music == "on":
    print("달립니다!")
    n = n + 1
    print("{}바퀴째입니다.".format(n))

    if n == 3:  # 3바퀴째면,
        music = "off"