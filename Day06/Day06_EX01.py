# Day06_EX01.py

favorite = [7, 5, 3, 1, 11]
         #  0  1  2  3  4  : favorite 리스트의 인덱스

# 1번자리에 777 끼워주세요. [7, 777, 5, 3, 1, 11]
# favorite[1] = 777
favorite.insert(1, 777)
print(favorite)

# [7, 777, 5, 3, 1, 11]
# 3을 빼주세요.
favorite.remove(3)
print(favorite)

# [7, 777, 5, 1, 11]
# 2번 자리를 빼주세요.
del favorite[2]
print(favorite)