#!/usr/bin/env python3
import math

# Парты

class01 = int(input('Введите количество учеников в первом классе '))
class02 = int(input('Введите количество учеников во втором классе '))
class03 = int(input('Введите количество учеников в третьем классе '))
print('Необходмиое количество парт => ', math.ceil(class01 / 2) + math.ceil(class02 / 2) + math.ceil(class03 / 2))
