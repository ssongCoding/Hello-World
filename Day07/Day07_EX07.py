# Computer 생성자 : 매개변수 회사 이름 -> 각 객체의 정보 company
# powerOn/Off 00컴퓨터가 켜졌습니다./꺼졌습니다.

class Computer:
    def powerOn(self):
        print("컴퓨터가 켜졌습니다.")

    def powerOff(self):
        print("컴퓨터가 꺼졌습니다.")

samsong = Computer()
samsong.powerOn()
samsong.powerOff()

LZ = Computer()
LZ.powerOn()
LZ.powerOff()