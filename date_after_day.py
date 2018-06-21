months_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]

while True:
    input_year = int(input("Podaj datę. Najpierw rok: "))
    input_month = int(input("Miesiąc: "))
    input_day =  int(input("Dzień: "))

    if input_month < 12 and input_month in months_31 and input_day == 31:
        print("Twoja data to: 01.", input_month +1, ".", input_year)
    elif input_month < 12 and input_month in month_30 and input_day == 30:
        print("Twoja data to: 01.", input_month +1,".", input_year)
    elif input_month < 12 and input_month == 2 and input_day == 29:
        if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 100 == 0 and input_year % 400 == 0):
            print("Twoja data to: 01.", input_month + 1, ".", input_year)
        else:
            print("Twoja data to: 01.", input_month + 1, ".", input_year)
    elif input_month < 12 and input_day < 30:
        print("Twoja data to: ",(input_day+1),".", input_month, ".", input_year)
    elif input_month == 12 and input_day == 31:
        print("Twoja data to: 01.01.", input_year+1)
    else:
        print("Coś jest nie tak. Spróbuj raz jeszcze: ")