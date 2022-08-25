l = [1, 2, 3, 4, 5]  # list
l2 = [6, 7, 8]
l3 = []
l4 = [13]

t = (1, 2, 3, 4, 5)  # tuple
t2 = (6, 7, 8)
t3 = ()
t4 = (13, )  # 튜플로 1개 만들 때

# 전체 출력
print(l)
print(t)

# 부분 출력 (슬라이싱)
print(l[1:4])  # 1번자리~3번자리까지
print(t[1:4])

# 요소 출력
print(l[2])
print(t[2])

l = l + l2
t = t + t2
print(l)
print(t)

# 요소 값 변경
l[2] = 10
# t[2] = 10

# 요소 1개 삭제
del l[0]
# del t[0]