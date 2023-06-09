"""
#15 8666
На числовой прямой даны два отрезка: P = [25; 50] и Q = [32; 47].
Укажите наибольшую возможную длину промежутка A, для которого формула
(¬ (x  принадлежит  A) → (x  принадлежит  P)) → ((x  принадлежит  A) → (x  принадлежит  Q))
тождественно истинна, то есть принимает значение 1 при любом значении переменной х
"""

# Данная задача в некотором роде похожа на предыдущий свой тип
# Здесь нам необходимо перебрать все возможные отрезки А с помощью циклов для обоих его концов
# Задаём циклы как-то так, чтобы описанные отрезки помещались внутри и были ещё несколько значений за ними
# То есть a < 25 и b > 47
answers = []
for a in range(0, 50):
    for b in range(a, 60):
        # -100 и 100 что-то типа -inf и inf,
        # опять же просто чтобы были какие-то числа x < 25 и x > 47
        for x in range(-100, 100):
            
            # Необходимо, чтобы для текущего отрезка [a, b] выражение было истино при всех возможных x
            check = ((not(a <= x <= b)) <= (25 <= x <= 50)) <= ((a <= x <= b) <= (32 <= x <= 47))

            # Если находится хоть одно x, что выражение ложно, то бросаем текущий отрезок
            if check == False:
                break
        # Если перебрались все x, то отрезок подходит под требования.
        else:
            # Добавляем его длину в список подходящих
            answers.append(b - a)

# Ответом будет максимальный из всех
print(max(answers))
