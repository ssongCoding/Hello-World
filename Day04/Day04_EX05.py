foods = ["돈까스", "삼겹살", "샐러드", "파스타"]

for food in foods:
    print(food)     # for 변수 in 리스트
                    #     변수 선언
                    #     이 변수를 for문이 알아서 요소를 하나씩 넣어주겠단 얘기!

num = [11, 22, 77, 99, 100]

for i in range(5):
    print(i)
    # 0 1 2 3 4 : i
    # 1 2 3 4 5 : i + 1
    # 2 4 6 8 10 : (i+1)*2
    print((i+1)*2)