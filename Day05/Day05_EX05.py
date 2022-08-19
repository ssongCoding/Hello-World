# 1단계. 종료가 입력될 때까지, while문 무한루프
# 2단계. 조회가 입력되면, basket의 내용을 출력

basket = ["딸기", "귤", "배", "파인애플"]  # 텅 빈 리스트
while True:  # 무한 루프
    print("<DIY 과일바구니 만들기> 메뉴를 입력하세요 : 조회 / 추가 / 종료")

    menu = input()
    if menu == "종료":
        break
    elif menu == "조회":  # 바구니에 딸기, 귤이 있습니다.
        print("바구니에", end = " ")
        for f in range(len(basket)-1): # [0, 1, 2]
            print("{}, ".format(basket[f]), end = "")
        # 저는 마지막 요소에만 ,를 빼주기로 했어요.
        # 저는 마지막 요소 전까지만 ,를 붙이기로 했어요.
        print(basket[len(basket)-1], end = "")
        print("이(가) 있습니다.")
    elif menu == "추가":
        print("바구니에 넣고 싶은 과일을 입력하세요.")
        fruit = input()
        basket.append(fruit)  # 끝 자리 4번 자리

        print("바구니에", end=" ")
        for f in range(len(basket)-1):
            print("{}, ".format(basket[f]), end="")
        print(basket[len(basket)-1], end="")

        print("이(가) 있습니다.")