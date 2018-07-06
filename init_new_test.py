class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __new__(cls,*args):
        print('on __new__')
        return super().__new__(cls)
       

if __name__ == '__main__':
    p = Person(1,2)
    print(p.age)