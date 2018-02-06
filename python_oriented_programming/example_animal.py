class Animal:
    def eat(self):
        print("%s eat " % self.name)

    def drink(self):
        print("%s drink " % self.name)

    def shit(self):
        print("%s shit " % self.name)

    def pee(self):
        print("%s pee " % self.name)


class Cat(Animal):
    def __init__(self, name):
        self.name = name
        self.breed = 'cat'

    def cry(self):
        print('cat crying')


class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.breed = 'dog'

    def cry(self):
        print('dog crying')


# ######### 执行 #########

c1 = Cat('小白家的小黑猫')
c1.eat()

c2 = Cat('小黑的小白猫')
c2.drink()

d1 = Dog('胖子家的小瘦狗')
d1.eat()