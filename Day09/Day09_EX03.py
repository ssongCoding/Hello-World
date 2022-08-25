input = [7, 1, 2, 3, 3, 2, 1]
inputLen = len(input)
output = []

index = 0
while index < inputLen:  # index < 5 : 0, 1, 2, 3, 4
    result = input.pop()  # pop() (1) 리스트 끝 요소를 제거해요.
                                # (2) 뭘 제거했는지 알려줘요.
    if result in output:
        pass  # ex.if~else, while, for ... 아무것도 안하고 싶을 때
    else:
        output.append(result)

    index = index + 1

print(output)