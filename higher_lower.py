import random

def int_input(prompt):

try:
    list_of_numbers = range(501)
    lucky_number = random.choice(list_of_numbers)
    count = 0

    while True:
        choice = int(input("Give me a lucky number from 0 to 500: "))
        if (choice == lucky_number):
            print("Bingo!")
            break
        elif (choice > lucky_number):
            print("The lucky number is lower")
            count += 1
        elif (choice < lucky_number):
            print("The lucky number is higher")
            count += 1


    print('You hit for ', count +1, 'times.')

except ValueError as err:
    print("Oczekiwano liczby. Nie można kontynuować.")
    print('Zwrócony błąd: ', err)