
            # 'Различие атрибутов класса и экземпляра' "

    # Ваша задача:
# 1 - Создайте новый класс Building с атрибутом total
# 2 - Создайте инициализатор для класса Building, который будет увеличивать атрибут количества созданных объектов класса
#     Building total (по примеру класса Lemming из урока)
# 3 - В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# 4 - Полученный код напишите в ответ к домашнему заданию

class Building:
    total = 0
    def __init__(self):
        Building.total += 1
        pass

for tot in range(1, 41):
    build = Building()
    print('Объекты класса № ', tot, build, build.total)


