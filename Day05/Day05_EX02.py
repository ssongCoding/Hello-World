# EX1. for 문을 이용해서, 0 1 2 3 4 5 6 7 을 출력해주세요.

"""
print("안녕하세요, \n저는 김송아입니다.")
print("감사합니다.", end = " ")
print("내일은 금요일입니다.")
"""
for n in range(8): # for 요소 in [0, 1, 2, 3, 4, 5, 6, 7]:
    print(n, end=" ")

# EX2. 리스트 ["월", "화", "수", "목", "금"]
#      len 함수를 이용해서 리스트 요소 개수를 구해주시고.
#      개수를 출력해주세요.
date = ["월", "화", "수", "목", "금"]

length = len(date)
print()
print(length)
"""
for d in date:   # for 요소 in 리스트:
    print(d)     #     print(요소) <- 한바퀴에 +1씩 올라가면서 출력
"""