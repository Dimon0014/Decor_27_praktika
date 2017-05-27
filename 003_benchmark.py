# coding=utf-8
def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs) # теоретически данное описание аргументов подходит
                                   # для любой функции, в том числе и без параметров( внизу
                                   # "vremja_vypolnenia()" как раз такой случай - без параметров
        print func.__name__, time.clock() - t #  в начале функция выполняется, а затем
        return res                            # результат возращается, тоесть тело функции
    return wrapper                           # выполняется в "wrapper"-е поэтому можно засечь
                                            # время выполнения этой функции

@benchmark
def vremja_vypolnenia():
    print "Привет"


vremja_vypolnenia()