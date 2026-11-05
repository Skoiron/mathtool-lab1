"""Сумма ряда."""

import math

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000
DIGITS = math.ceil(-math.log10(MAX_EPS))


def знак(n):
    if n % 2 == 0:
        return -1
    else:
        return 1


def слагаемое_sqplus(n):
    return знак(n) / (n * n + 1)


def слагаемое_third(n):
    return знак(n) / (3 * n)


# таблица рядов
FORMULAS = {
    "sqplus": (слагаемое_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third":  (слагаемое_third,  "S = 1/3 - 1/6 + 1/9 - 1/12 + ...")
}


def сумма_по_количеству(слагаемое, количество):
    результат = 0.0
    for n in range(1, количество + 1):
        результат = результат + слагаемое(n)
    return результат


def сумма_по_точности(слагаемое, eps):
    результат = 0.0
    n = 0
    while True:
        n = n + 1
        значение = слагаемое(n)
        результат = результат + значение
        if abs(значение) < eps:
            return результат, n
        if n >= MAX_ITERATIONS:
            raise ValueError("точность не достигнута")
