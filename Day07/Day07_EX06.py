
class Car:  # <자동차 만드는 설명서>
    def __init__(self, ms):     # 모든 클래스의 생성자는 __init__()
        self.maxSpeed = ms

    def info(self):
        print("내 최대 속력은 {} 입니다.".format(self.maxSpeed))

genesis = Car(300)
genesis.info()

tico = Car(150)
tico.info()