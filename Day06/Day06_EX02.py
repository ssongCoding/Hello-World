elevator = ["jason", "amy", "soni", "hope"]

elevator.pop() # del elevator[3]
print(elevator)
elevator.pop() # del elevator[2]
print(elevator)
elevator.pop() # del elevator[1]
print(elevator)
elevator.pop() # del elevator[0]
print(elevator)

elevator.append("kelly")
print(elevator)

elevator.append("bob")
print(elevator)

elevator.append("bill")
print(elevator)
"""
def pop():
    제일 마지막 원소를 제거하고,
    return pop() 앞에 있는 배열의 제일 마지막 원소
"""
print(elevator[-1])
elevator.pop()
print(elevator)

# 파이썬 스택, 지금 누가 내릴 차례인지
#                   = pop()을 당할 차례인지
#                   = 제일 마지막 요소가 무엇인지
