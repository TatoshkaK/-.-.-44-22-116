# Выполнила Красильникова Татьянна Дмитриевна. Группа 44-22-116. Вариант 6


import math
def calc(x: float) -> float:
    y: float = 0
    if x <= 0:
        y = math.sqrt(x) + (x**2)
    else:
        y = math.arctg(x)

def convert_number(x):
    """
    Фунуция преобразует число x в соответствии с заданной формулой.

    в случае успешного преобразования возвращает его результат.
    """

    try:
        if x <= 0:
            return math.sqrt(x) + math.sin(x)
        else:
            return math.sqrt(x + math.exp(x))
    except TypeError:
        return "<передано не число>"
