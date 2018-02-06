class D:
    def bar(self):
        print('D.bar')

class C(D):
    def bar(self):
        print('C.bar')

class B(D):
    pass
    # def bar(self):
    #     print('B.bar')

class A(B, C):
    pass
    # def bar(self):
    #     print('A.bar')

a = A()

# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去D类中找，如果D类中么有，则继续去C类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> D --> C
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了

a.bar()





class D2(object):
    def bar(self):
        print('D2.bar')


class C2(D2):
    def bar(self):
        print('C2.bar')


class B2(D2):
    pass
    # def bar(self):
    #     print('B2.bar')


class A2(B2, C2):
    pass
    # def bar(self):
    #     print('A2.bar')


a2 = A2()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去C类中找，如果C类中么有，则继续去D类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> C --> D
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a2.bar()