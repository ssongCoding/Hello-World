money = 5000
count = 0

def bus():
    global count, money
    count = count + 1
    money = money - 1250

bus()
print("저는 버스를 {}회 탔고, 남은 돈은 {}원입니다.".format(count, money))
