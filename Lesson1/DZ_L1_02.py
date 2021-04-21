seconds = int(input("Веедите кол-во секунд: "))
minutes = 0
hours = 0
#hou = min // 60
while seconds >= 60:
    seconds -= 60
    minutes += 1
while minutes >= 60:
    minutes -= 60
    hours += 1
print('{:0>2d}:{:0>2d}:{:0>2d}'.format(hours, minutes, seconds))
