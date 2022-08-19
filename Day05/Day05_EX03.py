MT_list = ["강아지", "송아지", "망아지", "김아지"]
        #     0        1        2        3

# ----- while문으로 요소 하나하나 출력 ----- #
i = 0
length = len(MT_list)  # 4

while i < length:
    print(MT_list[i], end = " ")
    i = i + 1

print()  # ENTER

# ----- for문으로 요소 하나하나 출력 ----- #
for m in MT_list:
    print(m, end=" ")

print()

"""
def len(List):
    return List의 요소 개수
"""

for k in range(len(MT_list)):  # <-- k : 0, 1, 2, 3
    print(MT_list[k], end=" ")