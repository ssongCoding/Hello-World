class Parent:
    money = 1000

    def inMyPocket(self):
        print("{}원이 있습니다.".format(Parent.money))


class Child(Parent):
    pass

dad = Parent()
print(dad.money)

son = Child()
print(son.money)
son.inMyPocket()

