# coding=utf-8
def isEven(value): return value % 2 == 0


# Альтернативный способ определения четности числа.
# плюсы - функция оперерирует только с нулевым битом исходного числа value

def isEvenAlter(value): return not bool(1 & value)
