# Номер на работу с файлами, потому вот немного теории про файлы.
# Открыть файл можно следующим образом
# file = open('path\\to\\file', 'r')

# Функция open принимает путь до файла и режим работы с ним и возвращает
# дескриптор этого файла, который можно воспринимать как сам файл

# Путь может быть глобальным и локальным
# Например, у меня есть файл из этого задания 17.txt. Если я зайду в его свойства,
# то там будет: Расположение C:\Users\enot\Рабочий стол\Python\EGE_classes\input_files
# Это глобальный путь
# open('C:\\Users\\enot\\Рабочий стол\\Python\\EGE_classes\\input_files\\17.txt', 'r')

# Локальный путь, это путь относительно запускаемого файла
# В папке EGE_classes находится текущий файл. Значит локальный путь будет input_files\17.txt
# open('input_files\\17.txt', 'r')

# Стоит заметить, что в windows разделителем является символ \, который используется
# для служебных символов вроде переноса строки \n или табуляции \t
# Потому чтобы он воспринимался просто как символ, приходится его дублировать \\


# Режимы работы с файлом:
# r - чтение
# w - создание и запись (если до этого был файл с таким же названием, он перезапишется)
# Остальные режимы, по идее, не понадобятся, но можно их нагуглить


# После работы с файлом его необходимо закрывать, чтобы избежать каких-либо негативных последствий
# f = open(...)
# работа с файлом
# f.close()

# Однако есть более удобная запись, которую я бы и предложил запомнить
# with open('path\\to\\file', 'r') as file:
#     работа с файлом
# Переменная file будет существовать только внутри блока with, а после его окончания
# файл автоматически закроется и переменная удалится


# Чтение данных из файла
# with open('path\\to\\file') as file:
    # Прочитать всё просто как одну строку
    # all_text = file.read()

    # Файл вида
    # 111
    # 222
    # 333
    # ...
    # Будет выглядеть как 111\n222\n333\n...

    # Считает текущую строку и переведёт указатель на следующую
    # current_line = file.readline()
    # Удобнее чем, read. Можно использовать с циклом, если знать длину файла
    # with open('input_files\\17.txt') as file:
    # for i in range(file_len):
    #     print(file.readline())
    # Но длину как правило и не узнаешь, пока не прочитаешь файл весь

    # Поэтому рекомендую именно последний способ чтения
    # В переменной окажется список со всеми строками файла, с которым можно удобно работать
    # all_lines = file.readlines()


"""
№17 38951
Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000.
Назовём парой два идущих подряд элемента последовательности.
Определите количество пар, в которых хотя бы один из двух элементов делится на 3,
а их сумма делится на 5. В ответе запишите два числа: сначала количество найденных пар,
а затем – максимальную сумму элементов таких пар.

Например, в последовательности (2 3 7 8 9) есть две подходящие пары: (2 3) и (3 7),
в ответе для этой последовательности надо записать числа 2 и 10.
"""

# Читаем файл
with open('input_files\\17_38951.txt') as file:
    str_numbers = file.readlines()

# Так как файл текстовый, то все строки выглядят как str. Например 3150 как '3150\n'
# Чтобы работать с ними как числами, нужно конвертировать их
int_numbers = []
for i in range(len(str_numbers)):
    # Берём строку по индексу, конвертируем, добавляем в другой список
    int_numbers.append(int(str_numbers[i]))


# Ищем максимум
max_sum = -1
# Считаем пары
num_pairs = 0

# Перебор пар как правило делается следующим образом:
# i - текущий элемент
# i + 1 - следующий
# Если range(len(int_numbers)) даёт индексы от первого, до последнего, 
# то i + 1 на последней итерации вылезет за границы.
# Поэтому range задаём на 1 меньше
for i in range(len(int_numbers) - 1):
    pair_sum = int_numbers[i] + int_numbers[i + 1]

    # Выражение делится первое или делится второе и делится сумма.
    # Здесь важно помнить порядок логических операций.
    # И делается раньше чем или. Однако выражение требует, чтобы или выполнилось первым
    if (int_numbers[i] % 3 == 0 or int_numbers[i + 1] % 3 == 0) and pair_sum % 5 == 0:
        num_pairs += 1

        # Обновляем максимум, если новымй max больше
        max_sum = max(pair_sum, max_sum)

print(num_pairs, max_sum)



"""
#17 47221
В файле содержится последовательность целых чисел.
Элементы последовательности могут принимать целые значения от -10000 до 10000 включительно.
Определите количество пар последовательности, в которых только одно число оканчивается на 3,
а сумма квадратов элементов пары не меньше квадрата максимального элемента последовательности,
оканчивающегося на 3. В ответе запишите два числа: сначала количество найденных пар,
затем максимальную из сумм квадратов элементов таких пар
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
"""

with open('input_files\\17_47221.txt') as file:
    str_numbers = file.readlines()

int_numbers = []
for i in range(len(str_numbers)):
    int_numbers.append(int(str_numbers[i]))


# Условие в задании 
# "...сумма квадратов элементов пары не меньше квадрата максимального элемента последовательности, 
# оканчивающегося на 3."
# говорит о том, что нам надо сначала найти максимальный элемент последовательности,
# да ещё и по условию
max_elem = -1
for i in range(len(int_numbers)):
    # Последнюю цифру числа можно получить в виде остатка при делении на 10
    if int_numbers[i] % 10 == 3:
        max_elem = max(int_numbers[i], max_elem)
max_square = max_elem ** 2


max_sum = -1
num_pairs = 0

for i in range(len(int_numbers) - 1):
    first = int_numbers[i]
    second = int_numbers[i + 1]

    # Только одно число оканчивается на 3
    first_condition = abs(first) % 10 == 3 and abs(second) % 10 != 3 or abs(first) % 10 != 3 and abs(second) % 10 == 3
    # Операция остатка от деления работает корректно только на положительных числах.
    # Поэтому необходимо брать положиельное представление числа перед делением
    # abs - модуль числа


    # Cумма квадратов элементов пары не меньше квадрата максимального элемента последовательности, 
    # оканчивающегося на 3
    square_sum = first ** 2 + second ** 2
    second_condition = square_sum >= max_square

    if first_condition and second_condition:
        num_pairs += 1

        max_sum = max(square_sum, max_sum)

print(num_pairs, max_sum)
