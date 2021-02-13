#!/usr/bin/env python3

#Составить UML-диаграмму деятельности и программу для решения задачи: Ввести список А из 10
#элементов, найти сумму элементов, больших 2 и меньших 20 и кратных 8, их количество и вывести результаты на
#экран

import sys


if __name__ == '__main__':
    A = list(map(float, input("Ввод:" ).split()))
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    sum = 0
    l = 0
    for item in A:
        if item > 2 and item < 20 and item % 8 == 0:
            sum += item
            l = l + 1
    print(sum)
    print(l)
