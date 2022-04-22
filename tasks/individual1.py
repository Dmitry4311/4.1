#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
"""
Поле first — дробное число; поле second — целое число, показатель степени. Реализовать
метод power() — возведение числа first в степень second. Метод должен правильно
работать при любых допустимых значениях first и second.
"""


class Number:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def read(self):
        self.first = float(input("Введите дробное число >> "))
        self.second = int(input("Введите целое число >> "))

    def display(self):
        print(f"Число  {self.first}, Степень {self.second}")

    def power(self):
        # Если число возводимое в степень равно 0
        first = (self.first ** self.second)
        if first == 0:
            raise ValueError
        else:
            return Number(first, self.second)


def make_number(first, second):
    if first == 0:
        raise ValueError
    else:
        return Number(first, second)


if __name__ == "__main__":
    newNumber = Number(3, 4)
    newNumber.display()
    newNumber.read()
    newNumber.display()
    make_number(3.4, 5)
    newNumber.power().display()

