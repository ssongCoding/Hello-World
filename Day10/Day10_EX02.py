
class Car:
    def ride(self):
        print("달립니다!")

    def stop(self):
        print("멈춥니다.")


class Bus(Car):
    # 부모 메소드와 같은 이름의 메소드 = 메소드 오버라이딩
    def ride(self):  # 부모 메소드 덮어쓰기
        super().ride() # super() : 부모 클래스 부르는 말
        print("씽씽!!")

    def fee(self):
        print("요금을 받았습니다.")

# tayo = Car()
tayo = Bus()
tayo.ride()
tayo.stop()
tayo.fee()
