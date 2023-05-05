"""
#23 15117
Исполнитель Фибо преобразует число на экране.

У исполнителя есть две команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 2

Первая команда увеличивает число на экране на 1, вторая увеличивает его на 2.

Программа для исполнителя Фибо  — это последовательность команд.

Сколько существует программ, которые преобразуют исходное число 3 в число 20
и при этом траектория вычислений содержит число 9 и не содержит числа 15?

Траектория вычислений  — это последовательность результатов выполнения всех команд программы.
Например, для программы 212 при исходном числе 7 траектория будет состоять из чисел 9, 10, 12.
"""

# В этом типе всё то же самое, что в 4-м, но совмещаются усложнения из 1-го и 2-го.
# Делаем то же самое, что в 1-м типе, но с доп условием из 2-го.


tree_nodes = [3]
necessary_node = 9
paths_to_necessary = 0

while len(tree_nodes) != 0:
    current_node = tree_nodes.pop(0)
    
    next_node = current_node + 1
    # Здесь пока нет смысла проверять, что нода это не 15,
    # так как мы сейчас идём только до 9
    # Но, вероятно, в других задачах, может оказаться, что избегаемая вершина
    # находится до обязательной
    if next_node < necessary_node:
        tree_nodes.append(next_node)
    elif next_node == necessary_node:
        paths_to_necessary += 1

    next_node = current_node + 2
    if next_node < necessary_node:
        tree_nodes.append(next_node)
    elif next_node == necessary_node:
        paths_to_necessary += 1


tree_nodes = [necessary_node]
target_node = 20
paths_to_target = 0
avoidable_node = 15

while len(tree_nodes) != 0:
    current_node = tree_nodes.pop(0)
    
    next_node = current_node + 1
    if next_node < target_node and next_node != avoidable_node:
        tree_nodes.append(next_node)
    elif next_node == target_node:
        paths_to_target += 1

    next_node = current_node + 2
    if next_node < target_node and next_node != avoidable_node:
        tree_nodes.append(next_node)
    elif next_node == target_node:
        paths_to_target += 1


print(paths_to_necessary * paths_to_target)
