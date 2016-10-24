#!/usr/bin/env python3

# Электронные часы
minutes = int(input('Введите количество минут '))
if minutes // 60 == 24:
    hours = 0
else:
    hours = minutes // 60
print('На часах ', hours, ' : ', minutes % 60)
