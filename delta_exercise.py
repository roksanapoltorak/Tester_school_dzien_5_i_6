a = float(input('Żeby policzyć deltę podaj a: '))
b = float(input('Żeby policzyć deltę podaj b: '))
c = float(input('Żeby policzyć deltę podaj jeszcze c: '))

delta = (b ** 2) - 4 * a * c
print("Delta to: ", delta)

if delta > 0:
    x_1 = (-b + delta ** 0.5) / (2 * a)
    x_2 = (-b - delta ** 0.5) / (2 * a)
    print('Rozwiązania to: ', x_1, " i ", x_2)

elif delta == 0:
    x_0 = -b / (2 * a)
    print("Rozwiązanie to: ", x_0)

else:
    print("Nie ma rozwiązania.")