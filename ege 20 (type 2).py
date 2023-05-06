"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней.
Игроки ходят по очереди, первый ход делает Петя.
За один ход игрок может добавить в одну из куч (по своему выбору) один камень
или увеличить количество камней в куче в два раза.
Например, пусть в одной куче 10 камней, а в другой 5 камней;
такую позицию в игре будем обозначать (10, 5).
Тогда за один ход можно получить любую из четырёх позиций: (11, 5), (20, 5), (10, 6), (10, 10).
Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней.

Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее 77.
Победителем считается игрок, сделавший последний ход, т. е. первым получивший такую позицию,
при которой в кучах будет 77 или больше камней.

В начальный момент в первой куче было семь камней, во второй куче  — S камней; 1 ≤ S ≤ 69.

Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Описать стратегию игрока  — значит, описать, какой ход он должен сделать в любой ситуации,
которая ему может встретиться при различной игре противника.
В описание выигрышной стратегии не следует включать ходы играющего по этой стратегии игрока,
не являющиеся для него безусловно выигрышными, т. е. не являющиеся выигрышными независимо от игры противника.

Найдите два таких значения S, при которых у Пети есть выигрышная стратегия,
причём одновременно выполняются два условия:

— Петя не может выиграть за один ход;
— Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.

Найденные значения запишите в ответе в порядке возрастания без разделительных знаков.
"""


s1 = 7
# Перебираем вторую кучу
for s2 in range(1, 70):

    # Первый ход Пети
    # Логика такая же, как и в первом типе
    first_turns = []
    
    # По условию Петя не должен выиграть на первый ход
    # Проверяем, что он не может сделать это ни с одной из куч
    if s1 * 2 + s2 < 77 and s2 * 2 + s1 < 77:
        # Если всё ок, то забираем все возможные ходы
        first_turns.append((s1 + 1, s2))
        first_turns.append((s1 * 2, s2))
        first_turns.append((s1, s2 + 1))
        first_turns.append((s1, s2 * 2))

    # Ход Вани
    # Все подходящие ходы Вани будем добавлять в список для следующего хода
    second_turns = []
    # Перебираем варианты первых ходов Пети
    for x1, x2 in first_turns:
        # Надо проверить, не выиграет ли Ваня с текущим вариантом хода Пети
        if x1 * 2 + x2 < 77 and x1 + x2 * 2 < 77:
            # Получается, сохраняем четвёрку пар чисел: все возможные комбинации хода Вани
            # исходящие из текущего варианта хода Пети
            second_turns.append(((x1 + 1, x2), (x1 * 2, x2), (x1, x2 + 1), (x1, x2 * 2)))

    # Второй ход Пети
    # Перебираем то, что осталось после хода Вани
    for var1, var2, var3, var4 in second_turns:
        # Попробуем немного уменьшить энтропию
        # Распакуем каждый вариант в отдельные переменные
        x1, x2 = var1
        # И сохраним лишь одно число - наивыгоднейший ход Пети из этого варианта
        var1 = max(x1 * 2 + x2, x2 * 2 + x1)

        x1, x2 = var2
        var2 = max(x1 * 2 + x2, x2 * 2 + x1)
        x1, x2 = var3
        var3 = max(x1 * 2 + x2, x2 * 2 + x1)
        x1, x2 = var4
        var4 = max(x1 * 2 + x2, x2 * 2 + x1)
        
        # В итоге если все эти варианты оказались победными, то это то, что искали
        if var1 >= 77 and var2 >= 77 and var3 >= 77 and var4 >= 77:
            print(s2)
