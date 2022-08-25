class Tree:
    def __init__(self):
        self.cursor = 1
        self.size = 8
        self.tree = [None] * self.size

    def add(self, item):  # isFull
        if not self.isFull():  # == if self.isFull() != True
            self.tree[self.cursor] = item
            self.cursor += 1  # self.cursor = self.cursor + 1

    def delete(self):
        if self.isEmpty() == False:
            self.tree[self.cursor-1] = [None]  # 다른 언어는 이 코드가 없어요.
            self.cursor = self.cursor - 1

    def isEmpty(self):
        if self.cursor == 1:
            True
        else:
            False

    def isFull(self):
        if self.cursor == self.size:
            True
        else:
            False

    def show_parents(self, position):
        # 루트 노드이면 안해줄거고.
        # position이 트리 범위 안에 들어오는지
        print("{}의 부모 노드의 값은 {}"
              .format(position, self.tree[position//2]))

    def show_left_child(self, position):
        # position * 2가 트리 범위 안에 들어오는지
        print(self.tree[position*2])

    def show_right_child(self, position):
        # position*2 + 1이 트리 범위 안에 들어오는지
        print(self.tree[position*2+1])

    def display(self):
        index = 1
        while index < self.cursor:
            print(self.tree[index], end=" ")
            index = index + 1

        print()
        # range 심화버전 : 시작 숫자, 끝 숫자
        # print(self.tree[1:self.cursor])

tree = Tree()
tree.add('a')
tree.add('b')
tree.add('c')
tree.add('d')
tree.add('e')
tree.add('f')
tree.add('g')
tree.display()  # None 'a' 'b' 'c' 'd' 'e' 'f' 'g'

tree.show_parents(3)  # 'a'
tree.show_parents(7)  # 'c'

tree.show_left_child(2)  # 4번 자리 : d
tree.show_right_child(2) # 5번 자리 : e

tree.delete()
tree.delete()
tree.delete()
tree.display()    # None 'a' 'b' 'c' 'd'