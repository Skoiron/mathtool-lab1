"""Численное интегрирование."""

import math

MAX_STEPS = 100000


def F_ratio(x):
    return x / (x + 1)


def F_root(x):
    return math.sqrt(x * x + 1)


# таблица функций: (функция, формула, low, high, границы_допустимы)
FUNCTIONS = {
    "ratio": (F_ratio, "F(x) = x / (x + 1)",   0.0,  20.0, True),
    "root":  (F_root,  "F(x) = sqrt(x^2 + 1)", -5.0,  5.0, False),
}


def интеграл(F, a, b, шагов):
    dx = (b - a) / шагов
    результат = 0.0
    for i in range(шагов):
        x = a + i * dx
        результат = результат + F(x) * dx
    return результат
