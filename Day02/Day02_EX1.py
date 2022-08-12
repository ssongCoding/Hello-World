def season(month):
    if month >= 9:
        print("가을입니다.")
    elif month >= 6:  # 9 > month >= 6
        print("여름입니다.")
    elif month >= 3:  # 6 > month >= 3
        print("봄입니다.")
    else:  # 3 > month
        print("겨울입니다.")

season(11)