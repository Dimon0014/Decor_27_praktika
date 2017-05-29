# coding=utf-8


import functools

def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time
    @functools.wraps(func)
    def wrapper1(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock() - t, "_дек1"
        return res

    return wrapper1 # по ходу я декорирую wrapper2, поэтому он мне всякую хрень выводит


def logging(func):
    """
    Декоратор, логирующий работу кода.
    (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
    """

    @functools.wraps(func)
    def wrapper2(*args, **kwargs):
        res = func(*args, **kwargs)
        if type(args[0])== str:
          a=''.join(args)  # tuple to string --кортеж в строку
          b=a.decode('utf8')
          print  func.__name__, b, kwargs, "логгер_дек2","{0} была вызвана: ".format(func.__name__)
        else: print func.__name__, args, kwargs, "логгер2"
        return res

    return wrapper2


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """

    @functools.wraps(func)  # они как-то передаются друг другу в общем эти декораторы с их функцией "wrapper"
    def wrapper3(*args, **kwargs):
        wrapper3.count += 1
        res = func(*args, **kwargs)
        print "{0} была вызвана: {1}x_дек3".format(func.__name__, wrapper3.count)
        return res

    wrapper3.count = 0
    return wrapper3


@benchmark  # этот декоратор выведен №3
@logging  # этот декоратор выведен №2
@counter # этот декоратор выведен №1
def reverse_string(string):  # функция выведена последней №4
    test = string.decode('utf8')
    a = ''.join(reversed(test))
    return a



print reverse_string('А роза упала на лапу Азора')
print reverse_string(
    "A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!")
print reverse_string.__name__
# выведет:
# reverse_string ('А роза упала на лапу Азора',) {}
# wrapper 0.0 --это типа время работы функции
# reverse_string была вызвана: 1x
# арозА упал ан алапу азор А

# reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!',) {}
# wrapper 0.0 --это тпа время работы функции
# reverse_string была вызвана: 2x
# !amanaP :lanac a ,noep a ,stah eros ,raj a ,hsac ,oloR a ,tur a ,mapS ,snip ,eperc a ,)lemac a ro( niaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,inoracam ,elacrep ,epins ,spam ,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,nalp a ,nam A

# В моем случае было выведенно это:
# reverse_string была вызвана: 1x
# wrapper ('\xd0\x90 \xd1\x80\xd0\xbe\xd0\xb7\xd0\xb0
# \xd1\x83\xd0\xbf\xd0\xb0\xd0\xbb\xd0\xb0 \xd0
# \xbd\xd0\xb0 \xd0\xbb\xd0\xb0\xd0\xbf\xd1\x83
# \xd0\x90\xd0\xb7\xd0\xbe\xd1\x80\xd0\xb0',) {}--а это типа--('А роза упала на лапу Азора',) {}
# wrapper 0.000249822253946 --это типа время работы функции
# <reversed object at 0x0000000002389278>--а это типа--арозА упал ан алапу азор А

# reverse_string была вызвана: 2x
# wrapper ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!',) {}
# wrapper 0.000314355595474
# <reversed object at 0x0000000002389278>