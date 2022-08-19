        #    0         1        2
fruits = ["apple", "banana", "peach"]
fruits.append("grape")  # 리스트 요소 1개 추가 append

length = len(fruits)  # 리스트 안 요소 갯수
print(length)

index = 0
while index < length:
    print(fruits[index])
    index = index + 1

print("----------------")

for i in fruits:  # for (요소) in (리스트 이름):
    print(i)        # 요소 개수만큼 반복!
                    # 자동으로 인덱스 +1 을 하면서
                    # 요소를 하나씩 꺼내 쓸거라는 소리