input = [7, 1, 2, 3, 3, 2, 1]
input.reverse()  # input 이 거꾸로 뒤집혀요 [1, 2, 3, 3, 2, 1, 7]
output = []

for i in input:
    if i not in output:
        output.append(i)

print(input)