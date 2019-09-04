import time


def time_decorator(func):
    print('init time decorator')

    def inner(*kws, **args):
        print(time.time())
        func(*kws, **args)
    
    return inner


@time_decorator
def say_hello(*kws, **args):
    print(kws)
    print(args)


# say_hello = time_decorator(say_hello)


def greeting_decorator(name):
    print('init greeting decorator')

    def wrapper(func):
        
        def inner(*kws, **args):
            print('hello, {}!'.format(name))
            func(*kws, **args)
        
        return inner
    
    return wrapper


@greeting_decorator('jyz')
def bar(*kws, **args):
    print(kws)
    print(args)


# bar = greeting_decorator('jyz')(bar)

if __name__ == '__main__':
    print('---execute main---')
    say_hello('foo', 'bar', name='jyz', id=123)
    bar('abc', 'def', name='jyz', id=234)
