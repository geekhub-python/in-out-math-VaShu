#!/usr/bin/env python3

# Дележ яблок
schoolboys = int(input('Введите количество учеников '))
apples = int(input('Введите количество яблок '))
print('Яблок у каждого ученика => ', apples // schoolboys)
print('Остаток яблок в корзине => ', apples % schoolboys)
