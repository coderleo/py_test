def wrapper(*dargs,**dkvargs):
    print(dkvargs)
    def outer(func):
        def inner(*args,**kvargs):
            print('start inner {}'.format(dkvargs.get('www',None)))
            return func(*args,**kvargs)
        print('end inner')
        return inner
    return outer

@wrapper(www=123)
def test(kkk=1):
    print("I'm test {}".format(kkk))

if __name__ == '__main__':
    test(kkk=222)