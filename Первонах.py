

from colorama import init
from colorama import Fore, Back, Style
init()

print(Back.YELLOW)

what = input("Что делаем? (+,-): " )

print(Back.GREEN)

a = float(input("Введи первое число"))
b = float(input("Введи второе число"))
#float - мы перебрасываем это число в ВЕЩЕСТВЕННОЕ
#if - ЭТО ЕСЛИ
if what == "+":
    c = a + b
    print("Результат: " + str(c))

