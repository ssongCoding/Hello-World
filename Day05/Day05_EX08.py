
class Calc:
    def plus(self, n1, n2):
        print(n1+n2)

    def minus(self, n1, n2):
        print(n1-n2)

    def multi(self, n1, n2):
        print(n1*n2)

    def divide(self, n1, n2):
        print(n1/n2) # n1//n2

casio = Calc()
casio.plus(7, 7)    # 14
casio.minus(10, 3)  # 7
casio.multi(5, 5)   # 25
casio.divide(10, 2) # 5.0 or 5
