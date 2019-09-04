# Python 装饰器

```python
import time


def time_decorator(func):
    """无参装饰器"""
    print('init time decorator')

    def inner(*kws, **args):
        print(time.time())
        func(*kws, **args)

    return inner


@time_decorator
def say_hello(*kws, **args):
    print(kws)
    print(args)


# 等价于:
# say_hello = time_decorator(say_hello)


def greeting_decorator(name):
    """带参装饰器"""
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


# 等价于:
# bar = greeting_decorator('jyz')(bar)

if __name__ == '__main__':
    print('---execute main---')
    say_hello('foo', 'bar', name='jyz', id=123)
    bar('abc', 'def', name='jyz', id=234)

```
