input = [7, 1, 2, 3, 3, 2, 1]
#       -7 -6 -5 -4 -3 -2 -1
inputLen = len(input)
output = []

index = -1
while index >= -inputLen:
    if input[index] not in output:  # output에 input[index] 값이 없으면,
        output.append(input[index])

    index = index -1

print(output)