dates_of_month = {
    "1월" : 31,
    "2월" : 28,
    "3월" : 31,
    "4월" : 30,
    "5월" : 31,
    "6월" : 30
}

while True:
    m = input() # 숫자만 ex. 1 or 2 or 6
    print("{}월은 {}일까지 있습니다.".format(m, dates_of_month[m + "월"]))