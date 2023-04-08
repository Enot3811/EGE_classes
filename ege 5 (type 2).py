"""
Автомат получает на вход пятизначное число. По этому числу строится новое число по следующим правилам.
1. Складываются отдельно первая, третья и пятая цифры, а также вторая и четвёртая цифры.
2. Полученные два числа записываются друг за другом в порядке неубывания без разделителей.

Пример. Исходное число: 63 179. Суммы: 6 + 1 + 9 = 16; 3 + 7 = 10. Результат: 1016.
Укажите наименьшее число, при обработке которого автомат выдаёт результат 723.
"""

# Мы пытаемся найти пятизначное число, которое удовлетворяет каким-то условиям
# Значит мы можем перебрать все пятизначные числа, и каждое из них проверить
for num in range(10000, 100000):
    # Необходимо раздробить число на цифры
    # Это можно сделать с помощью операции деления с остатком на 10 (% 10)
    # например 16 % 10 даст 6
    # так как при делении получается 1 целая и ещё 6 остаток

    # Так как далее значение числа будет изменяться, то стоит скопировать его
    # перед преобразованиями
    source_num = num

    digits = []
    for _ in range(5):
        # Получаем остаток
        remainder = num % 10
        # Добавляем его в список
        # (insert вместо appent, чтобы число не переворачивалось)
        digits.insert(0, remainder)
        # Чтобы получить следующую цифру, надо сдвинуть число на 1 разряд
        # Например 19 % 10 -> 9; 19 // 10 -> 1; 1 % 10 -> 1
        num = num // 10
    
    # 1-я, 3-я и 5-я
    second = digits[0] + digits[2] + digits[4]
    # 2-я и 4-я
    first = digits[1] + digits[3]

    # Чтобы записать 2 числа друг за другом, удобнее всего воспользоваться
    # строковым типом данных.
    # При складывании двух строк они склеиваются, а не сумируются как int
    result = str(first) + str(second)

    # Необходимо, чтобы получившееся число было равно 723
    if result == '723':  # В кавычках, так как result уже не цифра, а строка
        print(source_num)
        # Перебор идёт от меньшего к большему,
        # Значит первое подошедшее число и будет меньшим
        break
