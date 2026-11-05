"""Разбор параметров командной строки."""

import argparse
from calc import series, integration


def построить_разборщик():
    """Создаёт разборщик и возвращает его."""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool — расчёты над уравнениями и числовыми последовательностями",
        allow_abbrev=False,
    )

    subparsers = parser.add_subparsers(dest="command")

    # команда solve
    solve_parser = subparsers.add_parser(
        "solve",
        help="решение уравнения A*x^2 + B*x + C = 0",
        allow_abbrev=False,
    )
    solve_parser.add_argument("-a", type=int, help="коэффициент A")
    solve_parser.add_argument("-b", type=int, help="коэффициент B")
    solve_parser.add_argument("-c", type=int, help="коэффициент C")

    # команда stats
    stats_parser = subparsers.add_parser(
        "stats",
        help="показатели последовательности чисел",
        allow_abbrev=False,
    )
    stats_parser.add_argument(
        "--input",
        help="имя файла, из которого читаются числа",
    )

    # команда series
    series_parser = subparsers.add_parser(
        "series",
        help="сумма знакочередующегося ряда",
        allow_abbrev=False,
    )
    series_parser.add_argument(
        "--func",
        required=True,
        choices=sorted(series.FORMULAS.keys()),
        help="какой ряд суммировать",
    )
    group = series_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="сколько слагаемых сложить")
    group.add_argument("--eps", type=float, help="до какой величины слагаемого считать")

    # команда integrate
    integrate_parser = subparsers.add_parser(
        "integrate",
        help="численное интегрирование методом левых прямоугольников",
        allow_abbrev=False,
    )
    integrate_parser.add_argument(
        "--func",
        required=True,
        choices=sorted(integration.FUNCTIONS.keys()),
        help="какую функцию интегрировать",
    )
    integrate_parser.add_argument(
        "--from",
        dest="start",
        type=float,
        required=True,
        help="нижний предел интегрирования",
    )
    integrate_parser.add_argument(
        "--to",
        type=float,
        required=True,
        help="верхний предел интегрирования",
    )
    integrate_parser.add_argument(
        "--steps",
        type=int,
        required=True,
        help="на сколько прямоугольников делится отрезок",
    )

    return parser
