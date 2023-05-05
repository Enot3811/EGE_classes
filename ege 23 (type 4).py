"""
#23 3607
У исполнителя Калькулятор две команды, которым присвоены номера:

1. прибавь 2,
2. умножь на 5.

Первая из них увеличивает число на экране на 2, вторая  — увеличивает его в 5 раз.
Программа для Калькулятора  — это последовательность команд.
Сколько есть программ, которые число 2 преобразуют в число 50?
"""

# Данная задача о построении дерева. Чем-то похоже на 13 номер с нахождением
# количества возможных путей, только здесь вместо населённых пунктов будут
# значения текущего числа, а каждой стрелке будет присвоена одна из описанных
# операций

# Например, вот кусочек дерева из текущей задачи
#             2
#     +2 /     *5 \
#       4          10
#  +2 / *5\    +2 / *5\
#    6    20     12    50

# Мы будем программно строить такое дерево до тех пор, пока все его нижние
# узлы не станут больше или равны 50
# Например, правый узел на этом примере, где *5 два раза уже 50.
# Значит больше он уже не будет ветвиться.
# При построении дерева будем просто считать количество узлов, равных 50


number = 2
# Узлы дерева, которые мы хотим ветвить дальше будем хранить в списке
# Сразу добавляем первый узел
tree_nodes = [number]
answer = 0

# Пока у нас узлы, которые можно ветвить, крутим цикл
while len(tree_nodes) != 0:
    # На каждой итерации достаём из списка очередной узел
    current_node = tree_nodes.pop(0)
    
    # Делаем с текущим узлом все описанные операции для ветвления
    next_node = current_node + 2
    # Если получившийся новый узел ещё можно ветвить,
    if next_node < 50:
        # то добавляем его в список для последующей обработки
        tree_nodes.append(next_node)
    # Если он оказался равен 50,
    elif next_node == 50:
        # то считаем его, но уже не добавляем, как и те, что больше 50
        answer += 1

    # То же самое для второй операции
    next_node = current_node * 5
    if next_node < 50:
        tree_nodes.append(next_node)
    elif next_node == 50:
        answer += 1
        
print(answer)


"""
#23 6965
У исполнителя три команды, которым присвоены номера:

1. прибавь 1,
2. сделай чётное,
3. сделай нечётное.

Первая из них увеличивает на 1 число x на экране, вторая умножает это число на 2,
третья переводит число x в число 2x + 1.
Например, вторая команда переводит число 10 в число 20,
а третья переводит число 10 в число 21.

Программа для исполнителя – это последовательность команд.
Сколько существует программ, которые число 2 преобразуют в число 16?
"""

number = 2
tree_nodes = [number]
answer = 0

while len(tree_nodes) != 0:
    current_node = tree_nodes.pop(0)
    
    next_node = current_node + 1
    if next_node < 16:
        tree_nodes.append(next_node)
    elif next_node == 16:
        answer += 1

    next_node = current_node * 2
    if next_node < 16:
        tree_nodes.append(next_node)
    elif next_node == 16:
        answer += 1

    next_node = current_node * 2 + 1
    if next_node < 16:
        tree_nodes.append(next_node)
    elif next_node == 16:
        answer += 1
        
print(answer)
