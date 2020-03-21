what = input("Что делаем? (+,-): " )

a = float(input("Введи первое число"))
b = float(input("Введи второе число"))

#float - мы перебрасываем это число в ВЕЩЕСТВЕННОЕ

#if - ЭТО ЕСЛИ
if what == "+":
    c = a + b
    print("Результат: " + str(c))

elif what == "-":
    c = a - b
    print("Результат: " + str(c))

else:
    print("Выполнена неверная операция!")

