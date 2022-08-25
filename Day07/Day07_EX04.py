class Barista:
    # 생성자
    def __init__(self, n):  # 개발자가 직접 생성자를 구현
        self.name = n       # 자바 : this.name = name

    def hello(self):
        print("어서오세요. 저는 바리스타 {} 입니다.".format(self.name))

    def serve(self):
        print("커피 나왔습니다.")

barista = Barista("ssong")  # 생성자 호출 --> 객체가 변수를 갖고 태어납니다.
barista.hello()
barista.serve()