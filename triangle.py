a = 5
b = 3
c = 3

if a < 0 and b < 0 and c > 0:
    print("Nie da się utworzyć trojkata")
elif a + b > c and b + c > a and  a + c > b:
    print('Można utworzyć trójkąt z tych długości.')
else:
    print("Nie można utworzyć trójkąta.")