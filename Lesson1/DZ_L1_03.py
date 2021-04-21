while True:
    #цикл для повторного ввода если ввели число больше 10 или меньше 0
    number = int(input("Введите число:"))
    if number > 0 and number < 10:
        break
number2 = int(number * 11)
number3 = int(number * 111)
summa = int(number + number2 + number3)
print(summa)
