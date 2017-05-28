# coding=utf-8
def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock() - t
        return res

    return wrapper


def logging(func):
    """
    Декоратор, логирующий работу кода.
    (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res

    return wrapper


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print "{0} была вызвана: {1}x".format(func.__name__, wrapper.count)
        return res

    wrapper.count = 0
    return wrapper

import httplib


@benchmark
@logging
@counter
def get_random_futurama_quote():
    conn = httplib.HTTPConnection("slashdot.org:80")
    conn.request("HEAD", "/index.html")
    for key, value in conn.getresponse().getheaders():
        if key.startswith("x-b") or key.startswith("x-f"):
            return value
    return "Эх, нет... не могу!"


print get_random_futurama_quote()
print get_random_futurama_quote()

# outputs:
# get_random_futurama_quote () {}
# wrapper 0.02
# get_random_futurama_quote была вызвана: 1x
# The laws of science be a harsh mistress.
# get_random_futurama_quote () {}
# wrapper 0.01
# get_random_futurama_quote была вызвана: 2x
# Curse you, merciful Poseidon!

# В моем случае выведенно это:
# get_random_futurama_quote была вызвана: 1x
# wrapper () {}
# wrapper 0.43748472222
# Эх, нет... не могу!
# get_random_futurama_quote была вызвана: 2x
# wrapper () {}
# wrapper 0.333154842305
# Эх, нет... не могу!
