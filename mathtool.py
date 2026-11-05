
import math
import sys
from calc import equation, stats, series, integration
from cli import построить_разборщик


def обработать_solve(args):
    # заданы либо все три, либо ни одного
    if (args.a is not None or args.b is not None or args.c is not None) and \
       (args.a is None or args.b is None or args.c is None):
        print("ОШИБКА: укажите все три коэффициента либо ни одного", file=sys.stderr)
        return 1

    if args.a is None:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
            return 1
    else:
        a = args.a
        b = args.b
        c = args.c

    try:
        equation.проверить_коэффициенты({"A": a, "B": b, "C": c})
        kind, d, roots = equation.solve(a, b, c)
    except ValueError as error:
        print("ОШИБКА:", error, file=sys.stderr)
        return 1

    if kind == "квадратное":
        print("Уравнение квадратное")
        if d == int(d):
            print("Дискриминант:", int(d))
        else:
            print("Дискриминант:", d)
        if len(roots) == 2:
            print(f"x1 = {roots[0]:.3f}")
            print(f"x2 = {roots[1]:.3f}")
        elif len(roots) == 1:
            print(f"x = {roots[0]:.3f}")
        else:
            print("Действительных корней нет")
    else:
        print("Уравнение линейное")
        print(f"x = {roots[0]:.3f}")

    return 0


def прочитать_числа(источник):
    числа = []
    for строка in источник:
        for слово in строка.split():
            try:
                значение = float(слово)
            except ValueError:
                raise ValueError(f"{слово} не является числом")
            if not math.isfinite(значение):
                raise ValueError(f"{слово} не является конечным числом")
            if abs(значение) > stats.MAX_ABS:
                raise ValueError(f"значение {значение} вне допустимого диапазона")
            числа.append(значение)

    if len(числа) == 0:
        raise ValueError("последовательность пуста")
    if len(числа) > stats.MAX_COUNT:
        raise ValueError(f"количество чисел превышает {stats.MAX_COUNT}")
    return числа


def обработать_stats(args):
    try:
        if args.input is not None:
            with open(args.input, encoding="utf-8-sig") as handle:
                числа = прочитать_числа(handle)
        else:
            числа=[]
            while True:
            # числа = прочитать_числа(sys.stdin)
                a=input()
                if len(a)==0 :
                    break
                for i in a.split():
                    числа.append(int(i))
                pass

    except OSError:
        print("ОШИБКА: файл не открывается", file=sys.stderr)
        return 1
    except ValueError as error:
        print("ОШИБКА:", error, file=sys.stderr)
        return 1

    for подпись, функция, формат in stats.REPORT:
        значение = функция(числа)
        if значение is None:
            print(f"{подпись}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{подпись}: {значение:{формат}}")

    return 0


def обработать_series(args):
    if args.func not in series.FORMULAS:
        print("ОШИБКА: неизвестный ряд", file=sys.stderr)
        return 1

    слагаемое, формула = series.FORMULAS[args.func]

    if args.terms is not None:
        if not (1 <= args.terms <= series.MAX_TERMS):
            print("ОШИБКА: количество слагаемых вне диапазона", file=sys.stderr)
            return 1
        результат = series.сумма_по_количеству(слагаемое, args.terms)
        количество = args.terms
    else:
        if not (math.isfinite(args.eps) and 0 < args.eps <= series.MAX_EPS):
            print("ОШИБКА: точность вне диапазона", file=sys.stderr)
            return 1
        try:
            результат, количество = series.сумма_по_точности(слагаемое, args.eps)
        except ValueError as error:
            print("ОШИБКА:", error, file=sys.stderr)
            return 1

    print(формула)
    print("Слагаемых:", количество)
    print(f"Сумма ряда: {результат:.{series.DIGITS}f}")
    return 0


def обработать_integrate(args):
    if args.func not in integration.FUNCTIONS:
        print("ОШИБКА: неизвестная функция", file=sys.stderr)
        return 1

    F, формула, low, high, closed = integration.FUNCTIONS[args.func]
    a = args.start
    b = args.to
    шагов = args.steps

    # проверка параметров — до начала расчёта
    if not (math.isfinite(a) and math.isfinite(b)):
        print("ОШИБКА: пределы должны быть конечными числами", file=sys.stderr)
        return 1
    if a >= b:
        print("ОШИБКА: начальный предел не меньше конечного", file=sys.stderr)
        return 1
    if not (1 <= шагов <= integration.MAX_STEPS):
        print("ОШИБКА: количество шагов вне диапазона", file=sys.stderr)
        return 1

    if closed:
        if a < low or b > high:
            print("ОШИБКА: предел вне промежутка", file=sys.stderr)
            return 1
    else:
        if a <= low or b >= high:
            print("ОШИБКА: предел вне промежутка", file=sys.stderr)
            return 1

    результат = integration.интеграл(F, a, b, шагов)

    print(формула)
    print(f"Значение интеграла: {результат:.4f}")
    return 0


def main(argv=None):
    """Точка входа."""
    parser = построить_разборщик()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    try:
        if args.command == "solve":
            return обработать_solve(args)
        if args.command == "stats":
            return обработать_stats(args)
        if args.command == "series":
            return обработать_series(args)
        if args.command == "integrate":
            return обработать_integrate(args)
    except (ValueError, OSError) as error:
        print("ОШИБКА:", error, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
