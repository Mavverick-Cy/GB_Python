def my_func (a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "y can not be zero"
    except ValueError:
        return "enter only number"
print(my_func(int(input("Enter a = ")), int(input("Enter b = "))))