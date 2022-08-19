MT_list = ["강아지", "송아지", "망아지", "김아지"]

# ----- 리스트 insert(), remove() ----- #
# MT_list[1] = "하마" <-- 이건 자료구조의 추가가 아닙니다.
MT_list.insert(1, "하마")
MT_list.remove("망아지")


# ----- 리스트 sort(), sorted() ----- #
print(MT_list)
# MT_list.sort()  # 리스트를 정렬해서 교체 (기존 리스트 덮어쓰기)
sorted_MT_list = sorted(MT_list)

print(MT_list)
print(sorted_MT_list)

# ----- 리스트 count() ----- #
numList = [1, 1, 3, 5, 7, 1, 1, 1]
fruitList = ["apple", "banana", "apple"]

del fruitList[2]
# fruitList.remove("apple") <-- 원하는 위치의 요소를 삭제 불가능
print(fruitList)



one = numList.count(1)
a = fruitList.count("apple")
print(a)