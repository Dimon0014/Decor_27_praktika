# coding=utf-8
def logging(func):
    """
    Декоратор, логирующий работу кода.
    (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
    от меня - типа трассировка?
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs # трассер стоит после того как функция отыграла
        return res                        # типа он называет какая функция только что отыграла
    return wrapper                        # и какие параметры у нее были

@logging
def log_func1():
    print "я функционал log_func1"
@logging
def log_func2():
    print "я функционал log_func2"

log_func1()
log_func2()