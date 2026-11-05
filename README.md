# mathtool

Лабораторная работа № 2. Обработка числовых рядов.

## Команды

```
python mathtool.py solve -a 1 -b -3 -c 2
python mathtool.py stats --input numbers.txt
python mathtool.py series --func sqplus --terms 6
python mathtool.py series --func sqplus --eps 0.0001
python mathtool.py integrate --func ratio --from 0 --to 20 --steps 1000
```

## Структура

- mathtool.py — точка входа
- cli.py — разбор параметров
- calc/ — расчётная часть
