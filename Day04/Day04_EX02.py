num = [7, 8, 1, 5, 2, 7, 7]  # 인덱스 : 0~6

count = 0  # 7이 몇개 인지 담을 변수
index = 0  # 리스트 인덱스 역할을 할 변수
while index <= 6: # < 7
    if num[index] == 7:
        count = count + 1  # 0 -> 1 -> 2 -> 3 ...

    index = index + 1

print(count) # 3
