income = abs(float(input("Введите выручку фирмы ")))
expences = abs(float(input("Введите издержки фирмы ")))
income = round(income,2)
expences = round(expences,2)
if income > expences:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {income / expences:.2f}")
    workers = abs(int(input("Введите количество сотрудников фирмы ")))
    print(f"прибыль в расчете на одного сторудника сотавила {income / workers:.2f}")
elif income == expences:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")