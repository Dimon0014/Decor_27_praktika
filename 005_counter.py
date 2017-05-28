# coding=utf-8
def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """

    def wrapper(*args, **kwargs):
        wrapper.count += 1  # аккамулятор счетчика
        res = func(*args, **kwargs)
        print "{0} была вызвана: {1}x".format(func.__name__, wrapper.count)
        return res

    wrapper.count = 0 # устанока счетчика из counter(func) так как она(counter(func)) вызываетс
    return wrapper    # только один раз при присвоении ей функции которую она будет декорировать

@counter
def menja_poschitali():
    print "Раз"

menja_poschitali()
menja_poschitali()
menja_poschitali()