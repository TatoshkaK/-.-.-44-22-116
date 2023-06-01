# Выполнила Красильникова Татьяна Дмитриевна. Группа 44-22-116. Задание 6


import argparse
from functions import convert_numbers


parser = argparse.ArgumentParser(description="Введите числа для преобразования через запятую без пробела")
parser.add_argument("-n", "--numbers", help="Ввести числа для преобразования через запятую без пробела")

args = parser.parse_args()

if args.numbers:
    print(f"Введены числа: {args.numbers}")
    print(f"Результат преобразования: {convert_numbers(*args.numbers.split(','))}")