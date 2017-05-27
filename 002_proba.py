# coding=utf-8
# Во время отладки, в трассировочную информацию выводится __name__ функции.
def foo01():
    print "foo001"
    #a=1
cool=foo01
print cool.__name__
# выведет: foo01
print "после первого вывода"

# Однако, декораторы мешают нормальному ходу дел:
def bar_dec01(func):
    def wrapper():
        print "bar_dec001"
        return func()

    return wrapper


@bar_dec01
def foo0_1():
    print "foo001_"


print foo0_1.__name__ # по факту мы первой вызываем декоратор который возращает "wrapper"
# выведет: wrapper     # но фишка в том что "wrapper" в свою очередь возращает функцию
print "после второго вывода" # чье имя и должно появиться
                             # "functools" может нам с этим помочь

import functools


def bar_dec002(func):
    # Объявляем "wrapper" оборачивающим "func"
    # и запускаем магию:
    @functools.wraps(func) # что здесь происходит непонятно, то есть мы декорируем "wrapper"
    def wrapper():         # "wrapper" после этого будет запускаться с дополнительным функционалом
        print "bar_dec002" # после чего будет трассировщику выдавать имя декорируемой функции
        return func()      # как в общем то и положено

    return wrapper


@bar_dec002
def foo03():
    print "foo003"


print foo03.__name__
# выведет: foo03