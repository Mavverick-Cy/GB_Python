month_dict = {1: 'Январь',
              2: 'Февраль',
              3: 'Март',
              4: 'Апрель',
              5: 'Май',
              6: 'Июнь',
              7: 'Июль',
              8: 'Август',
              9: 'Сентябрь',
              10: 'Октябрь',
              11: 'Ноябрь',
              12: 'Декабрь'}
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима',
                2: 'Весна',
                3: 'Лето',
                4: 'Осень'}

month = int(input("Введите месяц по номеру "))

if month ==1 or month == 12 or month == 2:
        print(month_dict.get(month))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
        print(month_dict.get(month))
        print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
        print(month_dict.get(month))
        print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
        print(month_dict.get(month))
        print(seasons_list[3])
else:
        print("Такого месяца не существует")