import sys
import math

def validate_range(value, limit):
    return abs(value) <= limit

# 1. Справка
if len(sys.argv) == 1 or sys.argv[1] == "--help":
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print()
    print("Использование:")
    print("    python mathtool.py                          вывод справки")
    print("    python mathtool.py --help                   вывод справки")
    print("    python mathtool.py solve                    ввод коэффициентов и лимита с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2 -m 10000  решение с параметрами")
    print()
    print("Коэффициенты A, B, C и лимит M — целые числа.")
    sys.exit(0)

if sys.argv[1] != "solve":
    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    sys.exit(1)

# 2. Получение данных
if len(sys.argv) == 2:
    # Интерактивный режим: пользователь вводит всё сам
    a_str = input("Введите A: ")
    b_str = input("Введите B: ")
    c_str = input("Введите C: ")
    m_str = input("Введите максимальное значение (лимит) M: ")

elif len(sys.argv) == 10:
    # CLI режим: ожидаем solve -a A -b B -c C -m M (всего 10 элементов: индексы 0–9)
    if (sys.argv[3] != "-a" or sys.argv[5] != "-b"
            or sys.argv[7] != "-c" or sys.argv[9] != "-m"):
        print("ОШИБКА: неверный формат параметров", file=sys.stderr)
        sys.exit(1)
    a_str = sys.argv[3]
    b_str = sys.argv[5]
    c_str = sys.argv[7]
    m_str = sys.argv[9]
else:
    print("ОШИБКА: неверный набор параметров", file=sys.stderr)
    print("Используйте либо интерактивный режим, либо формат:", file=sys.stderr)
    print("  python mathtool.py solve -a <A> -b <B> -c <C> -m <M>", file=sys.stderr)
    sys.exit(1)

# 3. Преобразование в числа
try:
    A = int(a_str)
    B = int(b_str)
    C = int(c_str)
    M = int(m_str)
except ValueError:
    print("ОШИБКА: все значения должны быть целыми числами", file=sys.stderr)
    sys.exit(1)

if M < 0:
    print("ОШИБКА: лимит M должен быть неотрицательным", file=sys.stderr)
    sys.exit(1)

# 4. Проверка диапазона
if not (validate_range(A, M) and validate_range(B, M) and validate_range(C, M)):
    print("ОШИБКА: значение коэффициента выходит за установленный лимит", file=sys.stderr)
    sys.exit(1)

# 5. Решение уравнения
if A == 0 and B == 0:
    print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
    sys.exit(1)
elif A == 0:
    print("Уравнение линейное")
    x = -C / B
    print(f"x = {x:.3f}")
else:
    print("Уравнение квадратное")
    D = B * B - 4 * A * C
    print(f"D = {D}")

    if D > 0:
        x1 = (-B + math.sqrt(D)) / (2 * A)
        x2 = (-B - math.sqrt(D)) / (2 * A)
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")
    elif D == 0:
        x = -B / (2 * A)
        print(f"x = {x:.3f}")
    else:
        print("Действительных корней нет")
