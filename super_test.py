class A:
    def __init__(self):
        print('A start')
        print('A end')

class B(A):
    def __init__(self):
        print('B start')
       
        super(B,self).__init__()
        print('B end')
    def p(self):
        print('current B')
        super().p('111')
class C(A):
    def __init__(self):
        print('C start')
        super(C,self).__init__()
        print('C end')
    def p(self,pa):
        print('current C-{}'.format(pa))
class D(B,C):
    def __init__(self):
        print('D start')
        super(D,self).__init__()
        print('D end')

if __name__ == '__main__':
    d = D()
    # print(d.__mro__)
    print(D.__mro__)
    #执行顺序：
    d.p()
    print(type(D))