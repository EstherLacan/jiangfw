# coding:utf-8
from __future__ import print_function
bis = __builtins__.__dict__.items()


def filter_exception(item):
    if type(item[1]) == type:
        if issubclass(item[1], BaseException):
            return True
    return False

bis_without_exct = list(filter(filter_exception, bis))



print(u'共', len(bis_without_exct), u'个')
print()

for i in bis_without_exct:
    print(i)
