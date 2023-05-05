"""
#23 11358
Исполнитель А16 преобразует число, записанное на экране.
У исполнителя есть три команды, которым присвоены номера:

1. Прибавить 1
2. Прибавить 2
3. Умножить на 2

Первая из них увеличивает число на экране на 1, вторая увеличивает его на 2, третья умножает его на 2.
Программа для исполнителя А16 – это последовательность команд.

Сколько существует таких программ, которые исходное число 3 преобразуют в число 12
и при этом траектория вычислений программы содержит число 10?

Траектория вычислений программы — это последовательность результатов выполнения всех команд программы.
Например, для программы 132 при исходном числе 7 траектория будет состоять из чисел 8, 16, 18.
"""

# К этому типу справедлива вся теория из 4-го типа, но с дополнением в виде
# обязательного узла. Что-то такое же, вроде бы, было в 13 номере.

# Чтобы посчитать количество путей, проходящих через узел, нам необходимо
# изначально посчитать количество путей, приходящих к этому узлу, а потому уже
# от него количество путей до основной цели.

# При этом ответом будет произвдение количества путей до обязательного пункта
# на количество путей от обязательного пункта до цели.


# Воспользуемся тем же алгоритмом построения дерева, до обязательного пункта
number = 3
tree_nodes = [number]
necessary_node = 10
paths_to_necessary = 0

while len(tree_nodes) != 0:
    current_node = tree_nodes.pop(0)
    
    next_node = current_node + 1
    if next_node < necessary_node:
        tree_nodes.append(next_node)
    elif next_node == necessary_node:
        paths_to_necessary += 1

    next_node = current_node + 2
    if next_node < necessary_node:
        tree_nodes.append(next_node)
    elif next_node == necessary_node:
        paths_to_necessary += 1

    next_node = current_node * 2
    if next_node < necessary_node:
        tree_nodes.append(next_node)
    elif next_node == necessary_node:
        paths_to_necessary += 1
        

# А теперь тот же алгоритм, но до итоговой цели
tree_nodes = [necessary_node]
target_node = 12
paths_to_target = 0

while len(tree_nodes) != 0:
    current_node = tree_nodes.pop(0)
    
    next_node = current_node + 1
    if next_node < target_node:
        tree_nodes.append(next_node)
    elif next_node == target_node:
        paths_to_target += 1

    next_node = current_node + 2
    if next_node < target_node:
        tree_nodes.append(next_node)
    elif next_node == target_node:
        paths_to_target += 1

    next_node = current_node * 2
    if next_node < target_node:
        tree_nodes.append(next_node)
    elif next_node == target_node:
        paths_to_target += 1


print(paths_to_necessary * paths_to_target)
